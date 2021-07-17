from conftest import DATA
import pytest


@pytest.mark.parametrize('obj', DATA)
def test_allowed_kind_values(obj: dict):
    assert obj['kind'] in ('Pod', 'ServiceAccount', 'NetworkPolicy', 'Deployment', 'Job')


@pytest.mark.parametrize(
    'obj',
    filter(lambda x: x['kind'] == 'Deployment', DATA)
)
def test_non_root_deployments(obj: dict):
    assert obj['spec']['template']['spec']['securityContext']['runAsNonRoot']
