#the vehicle test suite with pytest

import pytest
from vehicles import Vehicle, Car, Bike, Truck


def test_do_wheelie():
	bikez = Bike("Ducati", 2, 280, 600, "Red and Orange", 10, True, True)
	assert "Wheeeeeiieeee" == bikez.do_wheelie()



