from sodapy import Socrata

# GET https://data.sccgov.org/resource/n9u6-aijz.json?app_token=5c7yGnp23fEA4F2b9CpnTsOCs&incident_datetime=2022-11-03T00:00:00.000

client = Socrata("data.sccgov.org", '5c7yGnp23fEA4F2b9CpnTsOCs')
results = client.get("n9u6-aijz", where="incident_datetime>'2022-11-03T00:00:00.000'", limit=20)

print(len(results))