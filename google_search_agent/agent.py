# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

def get_menu() -> dict:
    """Retrieves the menu of a restaurant.

    Returns:
        dict: A dictionary of items and their prices in Rupiah.   
    """
    return {
      "burger": 35000,
      "pizza": 88000,
      "salad": 35000,
      "soda": 15000,
      "dessert": 6000,
      }

#Function to get item to cart 
def add_to_cart(item: str, quantity: int) -> str:
    """Retrieves the item to cart.

    Args:
        item (str): The item to add.
        quantity (int): The quantity of the item.

    Returns:
        str: Confirmation message.   
    """
    return f"{quantity}{item}(s) added to your cart."

#Function to remove item to the cart
def remove_from_cart(item: str, quantity:int) -> str:
    """Remove the item in cart.

    Args:
        item (str): The item to remove.
        quantity (int): The quantity of the item.

    Returns:
        str: Confirmation message.   
    """
    return f"{quantity}{item}(s) remove from your cart." 

#Function to view the cart
def view_cart(cart:dict)-> str:
    """View the item in cart.

    Args:
        cart (dict): The cart containing items and ther quantity.

    Returns:
        str: A string representation of the cart.   
    """
    if not cart:
      return "Your cart is empty."
      items = [f"{item}: {quantity}" for item, quantity in cart.items()]
    return "Your cart contains:\n" + "\n".join(items)

def checkout(cart:dict) -> str:
    """Chekout the cart.

    Args:
        cart (dict): The cart containing items and their quantities.

    Returns:
        str: Confirmation message with total price.   
    """
    total_price = sum(get_menu()[item]* quantity for item, quantity in cart.items())
    return f"Your order has been placed. Total amount is Rp {total_price}"

root_agent = Agent(
   # A unique name for the agent.
   name="google_search_agent",
   # The Large Language Model (LLM) that agent will use.
   model="gemini-2.0-flash-exp", # if this model does not work, try below
   # model="gemini-2.5-flash-preview-native-audio-dialog",
   #model="gemini-2.0-flash-live-001",
   # A short description of the agent's purpose.
   description="Agent to answer questions using Google Search.",
   # Instructions to set the agent's behavior.
   instruction='''
   You are drive thru agent. You will help customers order food from menu.
   You can add, remove items from the cart and checkout. You can also view the cart.
   After checkout, you will return the total amount of order and instruct the customer to pick order on the next window.
   ''',
   # Add google_search tool to perform grounding with Google search.
   tools=[get_menu, add_to_cart, remove_from_cart, view_cart, checkout],
)
