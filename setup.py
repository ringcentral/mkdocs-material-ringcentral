from setuptools import setup, find_packages

setup(
    name="mkdocs-material-ringcentral",
    version="1.0.2",
    description="RingCentral 2026 brand layer plugin for MkDocs Material",
    packages=find_packages(),
    package_data={
        "mkdocs_material_ringcentral": [
            "assets/*",
            "templates/*",
        ],
    },
    install_requires=["mkdocs>=1.5"],
    entry_points={
        "mkdocs.plugins": [
            "material-ringcentral = mkdocs_material_ringcentral.plugin:RingCentralPlugin",
        ],
    },
)
