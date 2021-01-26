import argparse as ap
import hail
from pprint import pprint
import time

from hail_scripts.v01.utils.add_clinvar import download_and_import_latest_clinvar_vcf, CLINVAR_VDS_PATH
from hail_scripts.v01.utils.vds_utils import write_vds

p = ap.ArgumentParser()
p.add_argument("-g", "--genome-version", help="Genome build: 37 or 38", choices=["37", "38"], required=True)
args = p.parse_args()

hc = hail.HailContext(log="./hail_{}.log".format(time.strftime("%y%m%d_%H%M%S")))

vds = download_and_import_latest_clinvar_vcf(hc, args.genome_version)

pprint(vds.variant_schema)

output_vds_path = CLINVAR_VDS_PATH.format(genome_version=args.genome_version)

write_vds(vds, output_vds_path)
