''''import phonenumbers
from test import number 

from phonenumbers import geocoder
ch_nmber= phonenumbers.parse(number,"CH")

print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier
service_number= phonenumbers.parse(number,"RO")

print(carrier.name_for_number(service_number,"en"))

'''
import phonenumbers
from phonenumbers import geocoder, carrier
from test import number

# Replace this with a valid phone number string
#number = "+41791234567"  # Example number for Switzerland

# Parse the number for geolocation
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# Parse the number for carrier information
# Ensure the number is valid for the region specified
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
