#!/usr/bin/env python

from kubernetes.shell_utils import simple_run as run

for vcf_path in [
    "gs://seqr-reference-data/GRCh37/MPC/fordist_constraint_official_mpc_values.vcf.gz",
    "gs://seqr-reference-data/GRCh38/MPC/fordist_constraint_official_mpc_values.liftover.GRCh38.vcf.gz"
]:
    run(" ".join([
        "python gcloud_dataproc/v01/run_script.py",
        "--cluster mpc",
        "hail_scripts/v01/convert_vcf_to_vds.py",
        "{vcf_path}",
    ]).format(**locals()))
