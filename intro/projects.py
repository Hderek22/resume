"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
# Used to write the page in the app.py file
    st.title("Projects[(GitHub)](https://github.com/hderek22)")
    st.markdown(
    """

**Machine Learning Crypto Trading Algorithm/Bot[(Code)](https://github.com/Hderek22/machine_learning_crypto_algo.git)**
- Built a logistic regression model using Sklearn
- Connected to Alpaca Finance API's with trading signals based on market movement

**Blockchain Payment Processing Tool[(Code)](https://github.com/Hderek22/blockchain_payment_processing_tool.git)**
- Created a blockchain currency and built a Streamlit app for making payments with the new currency

**Crowdsale KaseiCoin[(Code)](https://github.com/Hderek22/CrowdsaleKaseiCoin.git)**
- Created ab ERC20 token - KasaiCoin
- Coded crowdsale for ERC20 Token

**Music NFT Minter[(Code)](https://github.com/Hderek22/Music-NFT-Minter.git)**
- This app was built as a solo project during ETH Globals Metabolism hackathon
- Utilizing Open Zeppelins ERC-721 Smart Contract, it allows the user to turn their own song into an NFT
- Built using Streamlit and NFT Storage IPFS protocol

        

""",
    unsafe_allow_html=True,
)
