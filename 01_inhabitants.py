# -*- coding: utf-8 -*-
from pprint import pprint

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from district.central_street.house1 import room1 as r1h1
from district.central_street.house1 import room2 as r2h1
from district.central_street.house2 import room1 as r1h2
from district.central_street.house2 import room2 as r2h2
room1_house1_residents = ",".join(r1h1.folks)
room2_house1_residents = ",".join(r2h1.folks)
room1_house2_residents = ",".join(r1h2.folks)
room2_house2_residents = ",".join(r2h2.folks)
print("В комнате room_1 живут: " + room1_house1_residents)
print("В комнате room_2 живут: " + room2_house1_residents)
print("В комнате room_1 живут: " + room1_house2_residents)
print("В комнате room_2 живут: " + room2_house2_residents)


