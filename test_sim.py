import TrafficDemand as TD
import logging
import subprocess
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    # <SUMO_HOME>/tools/detector/flowrouter.py -n input_net.net.xml -d detectors.xml -f flows20140520.csv -o routes.xml -e flows.xml -i 60
    cmd = 'python3 {script_path} -n {net_path} -d {detectors_path} -f {conf_path} -o {output_path} -e {flows_path} -i {interval}'.format(
        script_path=Path(os.getenv('SUMO_HOME', '/usr/share/sumo')) / Path('tools/detector/flowrouter.py'),
        net_path=Path.cwd() / Path('simulation/updated.net.xml'),
        detectors_path=Path.cwd() / Path('simulation/detectors.xml'),
        conf_path=Path.cwd() / Path('simulation/Data/Config/wcfg.csv'),
        output_path=Path.cwd() / Path('simulation/Data/Out/route50.xml'),
        flows_path=Path.cwd() / Path('simulation/Data/Out/flow50.xml'),
        interval=50
    )

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)

    stdout_value, stderr_value = proc.communicate()
    logger.info(repr(stdout_value))
    logger.error(repr(stderr_value))

    pass
