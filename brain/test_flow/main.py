import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.sse import sse_client

from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI
import os
import time

import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if root_dir not in sys.path:
    sys.path.append(root_dir)
print(root_dir)
from DeepEmbody.manager.eaios_decorators import package_init, mcp_start,eaios

@eaios.brain
def test_skill():
    return test_nv()

if __name__ == "__main__":
    print(test_skill())