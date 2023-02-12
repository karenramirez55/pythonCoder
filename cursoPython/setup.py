from setuptools import setup
#SETUP.PY es para trabajar con paquetes redistribuibles

setup(
    name="mi_primer_paquete",
    version="1.0", #cada vez q hacemos un cambio y lo volvemos a reempaquetar le vamos subiendo esta version
    description="primer paquete redistribuible",
    author="Ramirez Karen Denise",
    author_email="ramirezkarendenise@gmail.com",
    packages=["mi_primer_paquete"]
)
#cree mi primer paquete el cual ya se puede redistribuir pasandole el nombre del paquete
#por consola hacer : pip install dist/mi_primer_paquete

#instalamos setuptools de esta manera: sudo apt-get install python3-setuptools Carli27E contraseña sudo
# se supone que cualquier persona con el nombre de mi paquete ahora puede usarlo y yo usar uno tmb.
