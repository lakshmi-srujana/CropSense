import ee

ee.Initialize(project="gen-lang-client-0886857907")

img = ee.ImageCollection(
    "COPERNICUS/S2_SR_HARMONIZED"
).first()

print(
    "Successfully fetched test Sentinel-2 tile ID:",
    img.id().getInfo()
)