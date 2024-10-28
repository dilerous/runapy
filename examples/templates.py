from runai.client import RunaiClient

client = RunaiClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)

# Get all templates
print(client.templates.all())

# Print all environments
print(client.environment.all())

# Get the jupyter-lab environment resource
jupyter_lab = client.environment.get_by_name(environment_name="jupyter-lab")

# Get the cpu-only compute resource
cpu_id = client.compute.get_by_name(compute_name="cpu-only")

# Create a template named test4 with the compute cpu-only and the jupyter_lab environment
print(client.templates.create(
    name="my-template",
    scope="cluster",
    assets = {
        "environment": jupyter_lab['meta']['id'],
        "compute": cpu_id['meta']['id']
    }
))

# Get template asset ID by name
test1 = client.templates.get_by_name(template_name="my-template")
asset = test1['meta']['id']
print(asset)

# Get new compute asset ID by name
cpu_only = client.compute.get_by_name(compute_name="cpu-only")
compute_id = cpu_only['meta']['id']

# Update a template named test4 with the compute cpu-only and the jupyter_lab environment
print(client.templates.update(
    name="test1",
    asset_id=asset,
    assets = {
        "environment": id,
        "compute": compute_id
    }
))