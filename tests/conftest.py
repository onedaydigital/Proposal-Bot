"""Pytest configuration file."""
import pytest


@pytest.fixture
def proposal_bot():
    """Create a test instance of ProposalBot."""
    from proposal_bot import ProposalBot
    return ProposalBot()
