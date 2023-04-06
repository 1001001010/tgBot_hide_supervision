from yoomoney import Authorize

Authorize(
      client_id="F2F11DDAD877E9CF15C0843FF969D9897A8EBA9FFD3698E95BD8553807E31E27",
      redirect_uri="https://ya.ru",
      scope=["account-info",
             "operation-history",
             "operation-details",
             "incoming-transfers",
             "payment-p2p",
             "payment-shop",
             ]
      )
