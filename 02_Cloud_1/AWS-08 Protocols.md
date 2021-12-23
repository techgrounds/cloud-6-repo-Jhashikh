# [08 Protocols]
[Geef een korte beschrijving van het onderwerp]

## Key-terms
- OSI Model -Open System Interconnection
- SMTP -
- HTTP
- HTTPS
- TLS
- NetBIOS
- TCP
- UDP
- IPv4
- IPv6
- RS232
- 100 Base TX ]

## Opdracht :- 1.1 Hoe een HTTPS TCP/IP pakket opgebouwed is ? 


### Gebruikte bronnen

https://www.objc.io/issues/10-syncing-data/ip-tcp-http/]
https://www.cdw.com/content/cdw/en/articles/networking/types-of-network-protocols.html
https://www.sciencedirect.com/topics/computer-science/transport-protocol
https://medium.com/jspoint/a-brief-overview-of-the-tcp-ip-model-ssl-tls-https-protocols-and-ssl-certificates-d5a6269fe29e

## Opdracht :- 1.2 Begrijp wie bepaalt welke protocols wij gebruiken en wat je zelf moet doen om een nieuw protocol te introduceren.

### Gebruikte bronnen

https://www.oreilly.com/library/view/http-the-definitive/1565925092/ch04s01.html
https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:the-internet/xcae6f4a7ff015e7d:transporting-packets/a/transmission-control-protocol--tcp
https://www.techrepublic.com/article/exploring-the-anatomy-of-a-data-packet/

## Opdracht :- 1.3 Identificeer op zijn minst een protocol per OSI-Laag

### Gebruikte bronnen
[https://www.guru99.com/layers-of-osi-model.html.

## Opdracht :- 1.4 
Ontdek de reden over onbeschikkbaarheid van FB op 4 Oct 2021.

### Gebruikte bronnen 
https://www.techtarget.com/searchnetworking/feature/3-lessons-from-the-2021-Facebook-outage-for-network-pros
https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/
### Ervaren problemen
[Geen probleem.  ]

### Resultaat
1.1 HTTPS TCP/IP Pakket
HTTPS stands for HyperText Transfer Protocol Secure and but it is misleading in some ways. HTTPS protocol can not alone do the encryption of data, in fact, it depends on the SSL or TLS protocol layer.
![ClientHello](/00_includes/Cloud/ClientHelloMessage.png)
00_includes\Cloud\Client Hello Message.png
![HTTPSStructure](/00_includes/Cloud/HTTPSStructure.png)


1.4
Tijdens routine-onderhoud aan het backbone-netwerk kreeg een technicus die de capaciteit probeerde te beoordelen, een commando en veroorzaakte een cascade van technische problemen, volgens Santosh Janardhan, Vice-President Engineering en Infrastructuur van Facebook. Hij legde in een blogpost uit dat een interne audittool de verkeerde configuratie had moeten stoppen, maar een softwarefout zorgde ervoor dat de controle mislukte. De foutieve opdracht uitgevoerd via de backbone-routers en de verbinding met de datacenters van Facebook verbroken.
Dat veroorzaakte op zijn beurt de secundaire DNS- en BGP-problemen. Toen de DNS-servers van het bedrijf niet konden communiceren met de datacenters, trokken ze automatisch hun BGP-routeadvertenties in, waardoor ze zichzelf in feite van de virtuele kaart van internet verwijderden. Opeens was het alsof Facebook, Instagram en WhatsApp niet bestonden.

Om het nog erger te maken, vertrouwen de interne operationele tools van Facebook op de eigen infrastructuur en DNS van het bedrijf om te functioneren. Medewerkers hadden daarom geen toegang tot de systemen die ze normaal gesproken gebruiken om te werken en te communiceren, en het netwerkpersoneel kon de storing niet op afstand onderzoeken of oplossen via hun gebruikelijke methoden.
