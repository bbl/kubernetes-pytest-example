# kubernetes-pytest-example

This repository shows how you can use [Pytest](https://docs.pytest.org/en/6.2.x/) to unit test your Kubernetes YAML
files.

## Motivation

There are many good projects that help you to define "unit" tests for your Kubernetes manifests, e.g. [conftest](https://github.com/open-policy-agent/conftest),
[config-lint](https://github.com/stelligent/config-lint) or [polaris](https://github.com/FairwindsOps/polaris). But, if you don't like custom DSLs, or you're just already using Python, then you can get inspired
by simple examples from this repository.

## Overview

The [manifests.yaml](./manifests.yaml) file contains a sample Nginx ingress controller deployment.

The [conftest.py](./conftest.py) configures a `--file` flag for the `pytest` command. 

There are a few examples of tests in the [tests/test_manifests.py](tests/test_manifests.py) file, e.g.:

```python
@pytest.mark.parametrize('obj', DATA)
def test_allowed_kind_values(obj: dict):
    assert obj['kind'] in ('Pod', 'ServiceAccount', 'NetworkPolicy')
```

Here's the sample output:
```bash
obj = {'apiVersion': 'rbac.authorization.k8s.io/v1', 'kind': 'ClusterRole', 'metadata': {'annotations': {'helm.sh/hook': 'pr...ups': ['admissionregistration.k8s.io'], 'resources': ['validatingwebhookconfigurations'], 'verbs': ['get', 'update']}]}

    @pytest.mark.parametrize('obj', DATA)
    def test_allowed_kind_values(obj: dict):
>       assert obj['kind'] in ('Pod', 'ServiceAccount', 'NetworkPolicy', 'Deployment', 'Job', 'Service', 'Role')
E       AssertionError: assert 'ClusterRole' in ('Pod', 'ServiceAccount', 'NetworkPolicy', 'Deployment', 'Job', 'Service', ...)

tests/test_manifests.py:7: AssertionError
```

You can find the full output in the GitHub Actions history. 