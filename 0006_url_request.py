import urllib.request

warning_uri = (
    'https://forecast.weather.gov'
    'product.php?site=AKQ&product=SMW&issuedby=AKQ'
)

with urllib.request.urlopen(warning_uri) as source:
    forecast_text = source.read()








