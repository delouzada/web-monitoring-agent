import subprocess
import requests
from domain.entities import NetworkTestResult
from domain.repositories import NetworkTestResultRepository
from infrastructure.config.config_loader import config  # Importa configurações do arquivo externo
from infrastructure.persistence.connection_factory import SessionLocal

class NetworkTestService:
    def __init__(self, repository: NetworkTestResultRepository):
        self.repository = repository
        self.sites_to_test = config["monitoring"]["sites"]

    def ping_test(self, site):
        """Executa um ping no site e retorna a latência e perda de pacotes."""
        try:
            result = subprocess.run(
                ["ping", "-c", "4", site],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            output = result.stdout
            if "time=" in output:
                latencies = [float(line.split("time=")[-1].split(" ")[0])
                             for line in output.split("\n") if "time=" in line]
                avg_latency = sum(latencies) / len(latencies) if latencies else None
            else:
                avg_latency = None

            packet_loss_line = [line for line in output.split("\n") if "packet loss" in line]
            packet_loss = float(packet_loss_line[0].split("%")[0].split()[-1]) if packet_loss_line else None

            return avg_latency, packet_loss
        except Exception as e:
            print(f"Erro ao executar ping: {e}")
            return None, None

    def http_test(self, site):
        """Mede o tempo de resposta HTTP do site."""
        try:
            response = requests.get(f"http://{site}", timeout=10)
            return response.elapsed.total_seconds(), response.status_code
        except requests.RequestException:
            return None, None

    def run_tests(self):
        """Executa os testes de rede e armazena os resultados no banco de dados."""
        results = []
        for site in self.sites_to_test:
            latency, packet_loss = self.ping_test(site)
            response_time, status_code = self.http_test(site)

            result = NetworkTestResult(
                site=site,
                latency=latency,
                packet_loss=packet_loss,
                response_time=response_time,
                status_code=status_code
            )

            self.repository.save(result)  # Agora o método save existe corretamente
            results.append(result)

        return results
