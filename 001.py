from diagrams import Cluster, Diagram
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage
from diagrams.onprem.network import Haproxy
from diagrams.onprem.network import Internet
from diagrams.onprem.network import Nginx
from diagrams.onprem.database import PostgreSQL

with Diagram(show=False):
    users = Users("Users")
    application = Server("Loan application")

    with Cluster("Entrypoint"):
        entrypoint = [Haproxy(), Nginx()]

    with Cluster("Third party integrations"):
        integrations = [Internet(), PostgreSQL()]

    with Cluster("Datastore"):
        datastore = Storage() - Storage()

    users >> entrypoint >> application >> integrations
    application >> datastore
