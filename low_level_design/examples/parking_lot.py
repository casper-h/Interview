"""Parking lot: a reference skeleton for shape, not a solution to memorize.

The design choices worth noticing:

  - Spot size is an enum on the spot, and whether a vehicle fits is a method on the vehicle. Adding
    an electric-vehicle spot with charging means a new SpotType and a new Vehicle check, not edits
    scattered across the lot.
  - Pricing is a strategy behind an interface, injected into the lot. Hourly, flat-rate, and
    surge pricing are separate classes; the lot never grows a branch per pricing rule.
  - The lot owns its levels and a level owns its spots (composition), so the ownership is explicit.

The exercise: extend this to reserved spots, or to a monthly-pass holder who skips payment, and
check whether the change stays localized.
"""

from abc import ABC, abstractmethod
from enum import Enum


class SpotType(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


class Vehicle(ABC):
    def __init__(self, plate: str):
        self.plate = plate

    @abstractmethod
    def can_fit(self, spot_type: SpotType) -> bool:
        ...


class Motorcycle(Vehicle):
    def can_fit(self, spot_type: SpotType) -> bool:
        return True


class Car(Vehicle):
    def can_fit(self, spot_type: SpotType) -> bool:
        return spot_type in (SpotType.COMPACT, SpotType.LARGE)


class Bus(Vehicle):
    def can_fit(self, spot_type: SpotType) -> bool:
        return spot_type is SpotType.LARGE


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle: Vehicle | None = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def park(self, vehicle: Vehicle) -> None:
        self.vehicle = vehicle

    def vacate(self) -> None:
        self.vehicle = None


# --- pricing strategy: the extension point -----------------------------------

class PricingStrategy(ABC):
    @abstractmethod
    def price(self, minutes: int, spot_type: SpotType) -> float:
        ...


class HourlyPricing(PricingStrategy):
    def __init__(self, rate_per_hour: float):
        self.rate_per_hour = rate_per_hour

    def price(self, minutes: int, spot_type: SpotType) -> float:
        hours = -(-minutes // 60)  # round up
        return hours * self.rate_per_hour


class Level:
    def __init__(self, level_id: str, spots: list[ParkingSpot]):
        self.level_id = level_id
        self.spots = spots

    def find_free_spot(self, vehicle: Vehicle) -> ParkingSpot | None:
        return next(
            (s for s in self.spots if s.is_free() and vehicle.can_fit(s.spot_type)),
            None,
        )


class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot, issued_at: int):
        self.vehicle = vehicle
        self.spot = spot
        self.issued_at = issued_at


class ParkingLot:
    def __init__(self, levels: list[Level], pricing: PricingStrategy):
        self.levels = levels
        self.pricing = pricing
        self.active: dict[str, Ticket] = {}

    def park(self, vehicle: Vehicle, now: int) -> Ticket | None:
        for level in self.levels:
            spot = level.find_free_spot(vehicle)
            if spot is not None:
                spot.park(vehicle)
                ticket = Ticket(vehicle, spot, now)
                self.active[vehicle.plate] = ticket
                return ticket
        return None  # lot full for this vehicle size

    def exit(self, plate: str, now: int) -> float:
        ticket = self.active.pop(plate)
        minutes = (now - ticket.issued_at) // 60
        ticket.spot.vacate()
        return self.pricing.price(minutes, ticket.spot.spot_type)
