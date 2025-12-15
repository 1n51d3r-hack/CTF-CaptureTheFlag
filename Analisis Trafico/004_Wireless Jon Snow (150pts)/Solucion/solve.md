
para este desafio tenemos el archivo cap 


$ capinfos earthrealm-01-0ef04eb9b381e8b81fe0af600e2dad1e.cap
File name:           earthrealm-01-0ef04eb9b381e8b81fe0af600e2dad1e.cap
File type:           Wireshark/tcpdump/... - pcap
File encapsulation:  IEEE 802.11 Wireless LAN
File timestamp precision:  microseconds (6)
Packet size limit:   file hdr: 65535 bytes
Number of packets:   1081
File size:           271 kB
Data size:           253 kB
Capture duration:    53.138749 seconds
First packet time:   2017-09-08 12:59:25.523292
Last packet time:    2017-09-08 13:00:18.662041
Data byte rate:      4779 bytes/s
Data bit rate:       38 kbps
Average packet size: 234.93 bytes
Average packet rate: 20 packets/s
SHA1:                f5f299aa4fe79f82082678a6a890d379bbf973bf
RIPEMD160:           bbd4b26e39bf95d68ef78f9f899d65a9311dbe14
MD5:                 0ef04eb9b381e8b81fe0af600e2dad1e
Strict time order:   False
Number of interfaces in file: 1
Interface #0 info:
                     Encapsulation = IEEE 802.11 Wireless LAN (20 - ieee-802-11)
                     Capture length = 65535
                     Time precision = microseconds (6)
                     Time ticks per second = 1000000
                     Number of stat entries = 0
                     Number of packets = 1081
```

informacion relevante: Encapsulation = IEEE 802.11 Wireless LAN (20 - ieee-802-11)
(https://wiki.wireshark.org/HowToDecrypt802.11)
hay que desencriptar el tráfico


en busqueda de paquetes EAPOL , encontramos algunos mensajes, 4 en total

$ tshark -r earthrealm-01-0ef04eb9b381e8b81fe0af600e2dad1e.cap -Y "eapol || wlan.fc.type_subtype == 0x08"
  907  43.405495 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 EAPOL 133  Key (Message 1 of 4)
  908  43.420374 AskeyCom_aa:b4:64 → Objetivo_aa:aa:47 EAPOL 155  Key (Message 2 of 4)
  909  43.482361 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 EAPOL 161  Key (Message 3 of 4)
  910  43.485974 AskeyCom_aa:b4:64 → Objetivo_aa:aa:47 EAPOL 131  Key (Message 4 of 4)
  911  43.582232 AskeyCom_aa:b4:64 → Objetivo_aa:aa:47 EAPOL 147  Key (Group Message 2 of 2)

  
  desde tshark, buscamos el essid.

  
$ tshark -r earthrealm-01-0ef04eb9b381e8b81fe0af600e2dad1e.cap -Y "wlan.ssid"
  221  12.708667 Objetivo_aa:aa:47 → Htc_07:72:0f 802.11 411  Probe Response, SN=2935, FN=0, Flags=........, BI=100, SSID=Earthrealm
  235  12.789563 Objetivo_aa:aa:47 → Htc_07:72:0f 802.11 411  Probe Response, SN=2937, FN=0, Flags=........, BI=100, SSID=Earthrealm
  893  41.101883 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3239, FN=0, Flags=........, BI=100, SSID=Earthrealm
  894  41.104955 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3240, FN=0, Flags=........, BI=100, SSID=Earthrealm
  895  41.152572 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3242, FN=0, Flags=........, BI=100, SSID=Earthrealm
  896  41.198139 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3244, FN=0, Flags=........, BI=100, SSID=Earthrealm
  897  41.202235 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3245, FN=0, Flags=........, BI=100, SSID=Earthrealm
  898  41.569387 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3249, FN=0, Flags=........, BI=100, SSID=Earthrealm
  901  43.379927 AskeyCom_aa:b4:64 → Objetivo_aa:aa:47 802.11 52  Probe Request, SN=0, FN=0, Flags=........, SSID=Earthrealm
  902  43.388087 Objetivo_aa:aa:47 → AskeyCom_aa:b4:64 802.11 411  Probe Response, SN=3270, FN=0, Flags=........, BI=100, SSID=Earthrealm
  905  43.398870 AskeyCom_aa:b4:64 → Objetivo_aa:aa:47 802.11 89  Association Request, SN=2, FN=0, Flags=........, SSID=Earthrealm
```
con esto se confirma que usa WPA, ESSID es Earthrealm y el PSK esta dentro de la captura

herramientas para estas son hashcat y jhon the ripper, primero se captura el hash y luego crackearlo

el trabajo se hace online 
https://hashcat.net/cap2hccapx/](https://hashcat.net/cap2hccapx/

tambien tiene un clon en github https://github.com/hashcat/hashcat-utils, se compila y trabaja offline.

el resultado es esto:



```
$ cat 31535_1515072444.hccapx
HCPX
HRrthrealmóB[6ØMú%SRI\Ü¹äÁFªªG×wgðè
  éE©$W¼«Ãüº|!cª´dé?0bP÷³í٦ùD§æa5iI^9Æêàä{wþ
é?0bP÷³í٦ùD§æa5iI^9ÆêàäÝPòPòPòPòHCPX
HRrthrealmóB[6ØMú%SRI\Ü¹äÁFªªG×wgðè
  éE©$W¼«Ãüº|!cª´dé?0bP÷³í٦ùD§æa5iI^9Æêàä{wþ
é?0bP÷³í٦ùD§æa5iI^9ÆêàäÝPòPòPòPò
```
hay que buscar el password, usando seclist 

	hashcat --force -a 0 -m 2500 31535_1515072444.hccapx ~/Software/git/SecLists/Passwords/*txt
	
encuentra esto:

	a23151e7f4f232c4193bde5aa7969b52:e4c146aaaa47:002163aab464:Earthrealm:sysadmin1
	
	asi que ahora tenemos el valor de la key, pero hay que desencriptar el tráfico 
	wpa-pwd se ve asi: 
	
```
$ tshark -nr earthrealm-01-0ef04eb9b381e8b81fe0af600e2dad1e.cap -o wlan.enable_decryption:TRUE -o "uat:80211_keys:\"wpa-pwd\",\"sysadmin1:Earthrealm\"" -Y "ftp"
	  931  47.615997 192.168.1.39 → 192.168.1.100 FTP 112 64 Request: USER jon
  932  47.620093 192.168.1.39 → 192.168.1.100 FTP 121 64 Request: PASS Subzer0_2017
  934  47.626237 192.168.1.39 → 192.168.1.100 FTP 108 64 Request: FEAT
  938  47.633947 192.168.1.100 → 192.168.1.39 FTP 114 128 [TCP ACKed unseen segment] Response: 200 Noted.
  940  47.638013 192.168.1.39 → 192.168.1.100 FTP 107 64 [TCP Previous segment not captured] Request: PWD
  941  47.640091 192.168.1.100 → 192.168.1.39 FTP 133 128 [TCP ACKed unseen segment] Response: 257 "/" is current directory.
  943  47.675389 192.168.1.39 → 192.168.1.100 FTP 108 64 Request: NOOP
  945  47.675389 192.168.1.39 → 192.168.1.100 FTP 109 64 [TCP ACKed unseen segment] Request: CWD /
  946  47.675419 192.168.1.100 → 192.168.1.39 FTP 157 128 [TCP Previous segment not captured] Response: 250 CWD command successful. "/" is current directory.
  947  47.685147 192.168.1.100 → 192.168.1.39 FTP 150 128 [TCP ACKed unseen segment] [TCP Previous segment not captured] Response: 227 Entering Passive Mode (192,168,1,100,4,10)
  952  47.696380 192.168.1.39 → 192.168.1.100 FTP 108 64 [TCP ACKed unseen segment] [TCP Previous segment not captured] Request: MLSD
  953  47.697947 192.168.1.100 → 192.168.1.39 FTP 148 128 [TCP ACKed unseen segment] Response: 150 Opening data channel for directory list.
  958  47.736347 192.168.1.100 → 192.168.1.39 FTP 128 128 Response: 226 Transfer successful.
```
asi que tenemos ya listo el reto 
PASS Subzer0_2017 es el flag 
printf "Subzer0_2017" | md5sum
flag{edb158e665b0f1beb4fa798eb8303762}
