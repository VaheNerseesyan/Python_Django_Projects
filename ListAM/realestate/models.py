from django.db import models

LOCATION_AREA = (
    ("YV", "Yerevan"),
    ("ARM", "Armavir"),
    ("AR", "Ararat"),
    ("ART", "Ararat"),
    ("KT", "Kotayk"),
    ("SHI", "Shirak"),
    ("LR", "Lorri"),
    ("GK", "Geharkunik"),
    ("SY", "Syunik"),
    ("ARG", "Aragatsotn"),
    ("TV", "Tavush"),
    ("VD", "Vayoc Dzor"),
    ("IT", "International")
)

CURRENCY = (
    ("Armenian dram", "AMD"),
    ("United States Dollars", "USD")
)

CONSTRUCTION_TYPE = (
    ("Stone", "Stone"),
    ("Panels", "Panels"),
    ("Monolith", "Monolith"),
    ("Bricks", "Bricks"),
    ("Cassette", "Cassette"),
    ("Wooden", "Wooden")
)

NEW_CONSTRUCTION = (
    ("No", "No"),
    ("Yes", "Yes")
)

ELEVATOR = (
    ("Available", "Available"),
    ("Unavailable", "Unavailable")
)

THE_HOUSE_HAS = (
    ("Intercom entry", "Intercom entry"),
    ("Concierge", "Concierge"),
    ("Playground", "Playground")
)

PARKING = (
    ("Outdoor parking", "Outdoor parking"),
    ("Covered parking", "Covered parking"),
    ("Garage", "Garage")
)

NUMBER_OF_ROOMS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8+", "8+")
)

NUMBER_OF_BATHROOMS = (
    ("1", "1"),
    ("2", "2"),
    ("3+", "3+")
)

CEILING_HEIGHT = (
    ("2.5", "from 2.5 m"),
    ("2.6", "from 2.6 m"),
    ("2.7", "from 2.7 m"),
    ("2.75", "from 2.75 m"),
    ("2.8", "from 2.8 m"),
    ("3", "from 3 m"),
    ("3.2", "from 3.2 m"),
    ("3.5", "from 3.5 m")
)

BALCONY = (
    ("Not available", "Not available"),
    ("Open balcony", "Open balcony"),
    ("Closed balcony", "Closed balcony"),
    ("Multiple balconies", "Multiple balconies")
)

FURNITURE = (
    ("Available", "Available"),
    ("Not available", "Not available"),
    ("Partial furniture", "Partial furniture"),
    ("By agreement", "By agreement")
)

RENOVATION = (
    ("No Renovation", "No Renovation"),
    ("Old Renovation", "Old Renovation"),
    ("Partial Renovation", "Partial Renovation"),
    ("Cosmetic Renovation", "Cosmetic Renovation"),
    ("Euro Renovation", "Euro Renovation"),
    ("Designer Renovation", "Designer Renovation"),
    ("Major Renovation", "Major Renovation")
)

AMENITIES = (
    ("Television", "Television"),
    ("Air Conditioner", "Air Conditioner"),
    ("Internet", "Internet"),
    ("Parking space", "Parking space")
)

APPLIANCES = (
    ("Fridge", "Fridge"),
    ("Stove", "Stove"),
    ("Microwave", "Microwave"),
    ("Coffee maker", "Coffee maker"),
    ("Dishwasher", "Dishwasher"),
    ("Washing machine", "Washing machine"),
    ("Drying machine", "Drying machine"),
    ("Water heater", "Water heater"),
    ("Iron", "Iron"),
    ("Hair dryer", "Hair dryer")
)

WINDOW_VIEWS = (
    ("Yard view", "Yard view"),
    ("Street view", "Street view"),
    ("City view", "City view"),
    ("Park view", "Park view"),
    ("View of Ararat", "View of Ararat")
)

YES_NO = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("Negotiable", "Negotiable")
)

FLOORS_IN_THE_BUILDING = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4+", "4+")
)

TYPE = (
    ("Office space", "Office space"),
    ("Retail space", "Retail space"),
    ("Industrial and manufacturing", "Industrial and manufacturing"),
    ("Warehouse", "Warehouse"),
    ("Restaurant", "Restaurant"),
    ("Automotive service", "Automotive service"),
    ("Functioning business", "Functioning business"),
    ("Building", "Building"),
    ("Hotel", "Hotel"),
    ("Multifunctional space", "Multifunctional space"),
    ("Agricultural space", "Agricultural space"),
    ("Everything else", "Everything else")
)

LOCATION_FROM_THE_STREET = (
    ("First line", "First line"),
    ("Second line", "Second line"),
    ("Other", "Other")
)

ENTRANCE = (
    ("Common from the Street", "Common from the Street"),
    ("Common from the Courtyard", "Common from the Courtyard"),
    ("Separate from Street", "Separate from Street"),
    ("Separate from Courtyard", "Separate from Courtyards")
)

LEASE_TYPE = (
    ("Direct Lease", "Direct Lease"),
    ("Sublease", "Sublease")
)

MINIMUM_RENTAL_PERIOD = (
    ("1 month", "1 month"),
    ("2 month", "2 month"),
    ("3 month", "3 month"),
    ("4 month", "4 month"),
    ("6 month", "6 month"),
    ("9 month", "9 month"),
    ("1 year", "1 year"),
    ("2 years", "2 years"),
    ("3 years", "3 years"),
    ("5 years", "5 years"),
)

PREPAYMENT = (
    ("Without prepayment", "Without prepayment"),
    ("By agreement", "By agreement"),
    ("2 weeks", "2 weeks"),
    ("1 month", "1 month"),
    ("6 weeks", "6 weeks"),
    ("2 month", "2 month"),
    ("3 month", "3 month"),
    ("4 month", "4 month"),
    ("6 month", "6 month")
)

UTILITY_PAYMENTS = (
    ("Included", "Included"),
    ("Not included", "Not included"),
    ("By agreement", "By agreement")
)

"""
LongTermApartmentRentals...
"""


class LongTermApartmentRentals(models.Model):
    private = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    agency = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    verified_ads = models.BooleanField(default=False)
    price = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    currency = models.CharField(
        max_length=21,
        choices=CURRENCY
    )

    """Whereabouts"""
    location = models.CharField(
        max_length=15,
        choices=LOCATION_AREA,
        null=True,
        blank=True
    )
    street = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    house_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    hide_house_number_in_ad = models.BooleanField(default=False)
    """Building information"""
    construction_type = models.CharField(
        max_length=15,
        choices=CONSTRUCTION_TYPE,
        null=False,
        blank=False
    )
    new_construction = models.CharField(
        max_length=10,
        choices=NEW_CONSTRUCTION,
        null=False,
        blank=False
    )
    elevator = models.CharField(
        max_length=20,
        choices=ELEVATOR,
        null=False,
        blank=False
    )
    floors_in_building = models.CharField(
        max_length=10,
        choices=FLOORS_IN_THE_BUILDING,
        null=False,
        blank=False
    )
    the_house_has = models.CharField(
        max_length=25,
        choices=THE_HOUSE_HAS,
        null=True,
        blank=True
    )
    parking = models.CharField(
        max_length=25,
        choices=PARKING,
        null=True,
        blank=True
    )

    """Apartment information"""
    floor_area = models.PositiveSmallIntegerField(
        null=False,
        blank=False
    )
    number_of_rooms = models.CharField(
        max_length=10,
        choices=NUMBER_OF_ROOMS,
        null=False,
        blank=False
    )
    number_of_bathrooms = models.CharField(
        max_length=10,
        choices=NUMBER_OF_BATHROOMS,
        null=False,
        blank=False
    )
    ceiling_height = models.CharField(
        max_length=20,
        choices=CEILING_HEIGHT,
        null=False,
        blank=False
    )
    apartment_floor = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    balcony = models.CharField(
        max_length=20,
        choices=BALCONY,
        null=False,
        blank=False
    )
    furniture = models.CharField(
        max_length=25,
        choices=FURNITURE,
        null=False,
        blank=False
    )
    renovation = models.CharField(
        max_length=30,
        choices=RENOVATION,
        null=False,
        blank=False
    )
    amenities = models.CharField(
        max_length=30,
        choices=AMENITIES,
        null=True,
        blank=True
    )
    appliances = models.CharField(
        max_length=30,
        choices=APPLIANCES,
        null=True,
        blank=True
    )
    window_views = models.CharField(
        max_length=30,
        choices=WINDOW_VIEWS,
        null=True,
        blank=True
    )

    """House Rules"""
    children_are_welcome = models.CharField(
        max_length=20,
        choices=YES_NO,
        null=False,
        blank=False
    )
    pets_allowed = models.CharField(
        max_length=20,
        choices=YES_NO,
        null=False,
        blank=False
    )

    """Detail information"""
    optional_description = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )
    photos = models.ImageField(
        upload_to="media/product/",
        null=False,
        blank=False
    )

    """DATETIME"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    """Verification of Authenticity"""
    apartment_number = models.PositiveSmallIntegerField()
    cadastral_number = models.PositiveSmallIntegerField()
    supporting_document = models.ImageField(
        upload_to="media/documents/"
    )

    def __str__(self):
        return f"{self.location} - {self.price}"


class LongTermRentalsHouse(models.Model):
    private = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    agency = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    verified_ads = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)

    """Whereabouts"""
    location = models.CharField(
        max_length=15,
        choices=LOCATION_AREA,
        null=True,
        blank=True
    )
    street = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    house_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    hide_house_number_in_ad = models.BooleanField(default=False)

    """House information"""
    construction_type = models.CharField(
        max_length=15,
        choices=CONSTRUCTION_TYPE,
        null=False,
        blank=False
    )
    new_construction = models.CharField(
        max_length=10,
        choices=NEW_CONSTRUCTION,
        null=False,
        blank=False
    )
    floor_area = models.PositiveSmallIntegerField(
        null=False,
        blank=False
    )
    floors_in_building = models.CharField(
        max_length=10,
        choices=FLOORS_IN_THE_BUILDING
    )
    number_of_rooms = models.CharField(
        max_length=10,
        choices=NUMBER_OF_ROOMS,
        null=False,
        blank=False
    )
    number_of_bathrooms = models.CharField(
        max_length=10,
        choices=NUMBER_OF_BATHROOMS,
        null=False,
        blank=False
    )
    furniture = models.CharField(
        max_length=25,
        choices=FURNITURE,
        null=False,
        blank=False
    )
    parking = models.CharField(
        max_length=25,
        choices=PARKING,
        null=False,
        blank=False
    )
    renovation = models.CharField(
        max_length=30,
        choices=RENOVATION,
        null=False,
        blank=False
    )
    amenities = models.CharField(
        max_length=30,
        choices=AMENITIES,
        null=True,
        blank=True
    )
    appliances = models.CharField(
        max_length=30,
        choices=APPLIANCES,
        null=True,
        blank=True
    )

    """Lot information"""
    land_area = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )

    """House Rules"""
    children_are_welcome = models.CharField(
        max_length=20,
        choices=YES_NO,
        null=False,
        blank=False
    )
    pets_allowed = models.CharField(
        max_length=20,
        choices=YES_NO,
        null=False,
        blank=False
    )

    """Detailed information"""
    optional_description = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )
    photos = models.ImageField(
        upload_to="media/product/",
        null=False,
        blank=False
    )

    """DATETIME"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    """Verification of Authenticity"""
    apartment_number = models.PositiveSmallIntegerField()
    cadastral_number = models.PositiveSmallIntegerField()
    supporting_document = models.ImageField(
        upload_to="media/documents/"
    )

    def __str__(self):
        return f"{self.location} - {self.price}"


class LongTermRentalsCommercialProperties(models.Model):
    private = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    agency = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    verified_ads = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)

    """Whereabouts"""
    location = models.CharField(
        max_length=15,
        choices=LOCATION_AREA,
        null=True,
        blank=True
    )
    street = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    house_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    """Property information"""
    info_type = models.CharField(
        max_length=50,
        choices=TYPE,
        null=False,
        blank=False
    )
    floor_area = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )
    furniture = models.CharField(
        max_length=25,
        choices=FURNITURE,
        null=False,
        blank=False
    )
    elevator = models.CharField(
        max_length=20,
        choices=ELEVATOR,
        null=False,
        blank=False
    )
    location_from_the_street = models.CharField(
        max_length=30,
        choices=LOCATION_FROM_THE_STREET,
        null=False,
        blank=False
    )
    entrance = models.CharField(
        max_length=50,
        choices=ENTRANCE,
        null=False,
        blank=False
    )
    parking = models.CharField(
        max_length=25,
        choices=PARKING,
        null=True,
        blank=True
    )

    """Deal Terms"""
    lease_type = models.CharField(
        max_length=50,
        choices=LEASE_TYPE,
        null=False,
        blank=False
    )
    minimum_rental_period = models.CharField(
        max_length=50,
        choices=MINIMUM_RENTAL_PERIOD,
        null=False,
        blank=False
    )
    prepayment = models.CharField(
        max_length=50,
        choices=PREPAYMENT,
        null=False,
        blank=True
    )
    utility_payments = models.CharField(
        max_length=50,
        choices=UTILITY_PAYMENTS,
        null=False,
        blank=True
    )

    """Detailed Information"""
    optional_description = models.TextField(
        max_length=1000
    )
    photos = models.ImageField(
        upload_to='media/product'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)


class LongTermRentalsLand(models.Model):
    private = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    agency = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    verified_ads = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    prepayment = models.CharField(
        max_length=50,
        choices=PREPAYMENT
    )

    """Whereabouts"""
    location = models.CharField(
        max_length=15,
        choices=LOCATION_AREA,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    """Lot Information"""
    info_type = models.CharField(
        max_length=50,
        choices=LEASE_TYPE,
        null=False,
        blank=False
    )
    land_area = models.PositiveSmallIntegerField(
        null=False,
        blank=False
    )

    """Service Lines"""
    electricity = models.BooleanField(default=False)
    water_supply = models.BooleanField(default=False)
    natural_gas = models.BooleanField(default=False)
    sewerage = models.BooleanField(default=False)

    """Detailed information"""
    description = models.TextField(
        max_length=1000,
        null=False,
        blank=False
    )
    photo = models.ImageField(
        upload_to="media/product",
        null=False,
        blank=False
    )

    """DATETIME"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location} - {self.price}"


"""..."""
