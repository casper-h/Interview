"""Logging framework: levels, formatters, and sinks composed cleanly.

This is the reusable-component style of problem that weighs more heavily at the senior level and
above: the signal is a clean, extensible library other engineers build on, not a real-world domain.

The design choices worth noticing:

  - Formatter is a Strategy: plain text, JSON, or a custom shape are separate classes, and the
    logger neither knows nor cares which one it holds.
  - Sink is an interface (console, file, network), so where a record goes is orthogonal to how it is
    formatted. A logger fans out to many sinks.
  - Level filtering lives in one place. A record below the threshold is dropped before formatting, so
    formatting cost is not paid for suppressed logs.
  - A sink can be wrapped by a Decorator (here, an async buffering sink) that adds behavior without
    changing the sink interface.

The exercise: add a sink that batches and flushes on a size or time threshold, or a formatter that
redacts fields, and confirm neither change touches the logger or the other sinks.
"""

from abc import ABC, abstractmethod
from enum import IntEnum


class Level(IntEnum):
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40


class Record:
    def __init__(self, level: Level, message: str, timestamp: float):
        self.level = level
        self.message = message
        self.timestamp = timestamp


# --- formatting strategy -----------------------------------------------------

class Formatter(ABC):
    @abstractmethod
    def format(self, record: Record) -> str:
        ...


class TextFormatter(Formatter):
    def format(self, record: Record) -> str:
        return f"{record.timestamp} [{record.level.name}] {record.message}"


class JsonFormatter(Formatter):
    def format(self, record: Record) -> str:
        # A real implementation would use json.dumps; kept inline for shape.
        return (
            '{'
            f'"ts": {record.timestamp}, '
            f'"level": "{record.level.name}", '
            f'"msg": "{record.message}"'
            '}'
        )


# --- sinks -------------------------------------------------------------------

class Sink(ABC):
    @abstractmethod
    def write(self, line: str) -> None:
        ...


class ConsoleSink(Sink):
    def write(self, line: str) -> None:
        print(line)


class FileSink(Sink):
    def __init__(self, path: str):
        self.path = path

    def write(self, line: str) -> None:
        # Open in append mode and write; kept as a signature for the skeleton.
        ...


class AsyncSink(Sink):
    """Decorator: buffers and flushes on a background thread, wrapping any sink."""

    def __init__(self, inner: Sink, buffer_size: int):
        self.inner = inner
        self.buffer_size = buffer_size
        self._buffer: list[str] = []

    def write(self, line: str) -> None:
        self._buffer.append(line)
        if len(self._buffer) >= self.buffer_size:
            self.flush()

    def flush(self) -> None:
        for line in self._buffer:
            self.inner.write(line)
        self._buffer.clear()


class Logger:
    def __init__(self, min_level: Level, formatter: Formatter, sinks: list[Sink]):
        self.min_level = min_level
        self.formatter = formatter
        self.sinks = sinks

    def log(self, level: Level, message: str, now: float) -> None:
        if level < self.min_level:
            return  # filtered before any formatting cost is paid
        line = self.formatter.format(Record(level, message, now))
        for sink in self.sinks:
            sink.write(line)

    def info(self, message: str, now: float) -> None:
        self.log(Level.INFO, message, now)

    def error(self, message: str, now: float) -> None:
        self.log(Level.ERROR, message, now)
