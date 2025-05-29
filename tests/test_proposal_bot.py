"""
Test suite for ProposalBot.
"""
import pytest
from proposal_bot import ProposalBot

def test_proposal_bot_initialization():
    """Test that ProposalBot can be initialized."""
    bot = ProposalBot()
    assert isinstance(bot, ProposalBot)
