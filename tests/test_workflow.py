#! /usr/bin/env python3
# syntax=python tabstop=4 expandtab

import snakemake

from BALSAMIC.utils.cli import get_snakefile


def test_workflow_tumor_normal(tumor_normal_config):
    # GIVEN a sample config dict and snakefile
    workflow = 'paired'
    snakefile = get_snakefile(workflow)
    config_json = tumor_normal_config

    # WHEN invoking snakemake module with dryrun option
    # THEN it should return true
    assert snakemake.snakemake(snakefile,
                               configfile=config_json,
                               dryrun=True)


def test_workflow_tumor_only(tumor_only_config):
    # GIVEN a sample config dict and snakefile
    workflow = 'single'
    snakefile = get_snakefile(workflow)
    config_json = tumor_only_config

    # WHEN invoking snakemake module with dryrun option
    # THEN it should return true
    assert snakemake.snakemake(snakefile,
                               configfile=config_json,
                               dryrun=True)


def test_workflow_qc(tumor_normal_config, tumor_only_config):
    # GIVEN a sample config dict and snakefile
    workflow = 'qc'
    snakefile = get_snakefile(workflow)

    # WHEN invoking snakemake module with dryrun option
    # THEN it should return true
    for config_json in (tumor_normal_config, tumor_only_config):
        assert snakemake.snakemake(snakefile,
                                   configfile=config_json,
                                   dryrun=True)
