"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
# Used to write the page in the app.py file
    st.title("Projects[(GitHub)](https://github.com/hderek22)")
    st.markdown(
    """

**Music NFT Minter[(Video demonstration)](https://ethglobal.com/showcase/gemgroove-music-minter-xkfyn)**
- Award winning app for ETH Globals Metabolism hackathon
- Utilizing Open Zeppelins ERC-721 Smart Contract, this app allows the user to turn their own song into an NFT
- Built using Streamlit and NFT Storage IPFS protocol

**Machine Learning Crypto Trading Algorithm/Bot[(Code)](https://github.com/Hderek22/machine_learning_crypto_algo.git)**
- A logistic regression model using Sklearn
- Connected to Alpaca Finance API's with trading signals based on market movement

**Blockchain Payment Processing Tool[(Code)](https://github.com/Hderek22/blockchain_payment_processing_tool.git)**
- A blockchain Streamlit app for making payments with new currency

**Crowdsale KaseiCoin[(Code)](https://github.com/Hderek22/CrowdsaleKaseiCoin.git)**
- An ERC20 token - KasaiCoin
- Crowdsale for ERC20 Token


""",
    unsafe_allow_html=True,
)
