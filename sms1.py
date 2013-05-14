import pygvoicelib
username=<I put my username here as a string>
apppass="uqyvjchgxflldbgw"
auth_token="DQAAAMkAAADd1qrFmbULOs38GccNnagncAFI85nQ60056hZFWFlzbzpJEzkOQFsK9KgylTl_x_b6AAT0d7ZmzZlzUKQInjnGk-TkyQ6DKiw9NMXrie4QLaEiB9zvwr49yHwRuO-d-vEmrFCq2Fk0b_H7RFaCkNIbQ2oXVDSdlpyucXSpr-EhvI6V2SEs5FXUweqj8YeHzbY8iyQ_qyTmsuKc8-pXXi8OEIxslYht7pZ78_pngDfpfiikhsR_qDNSEgSKnH5zXx2RXVeKQgj7aEdI_EWJJ8_F"
rnr_se="QkQNZ3VWXipzMOite2NGlMasH+k="
client = pygvoicelib.GoogleVoice(username,apppass,auth_token,rnr_se)
#replace number with phone number below
client.sms(<put my number here>,"test")

