ORACLE_QRY = """
select
MAC_ADDRESS,
STB_ID 
from
HANAROCMS.PHYSICAL_STB
where
mac_address in (%s)
"""