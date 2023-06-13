
# exposuredetect🕵
  
exposuredetect is a straightforward Python 3 tool leveraging the CriminalIP API to effortlessly discover open databases, identify misconfigurations, and automatically detect vulnerabilities. Moreover, you can incorporate specific search (product,vulnerabilities,misconfigurations) directly into the script.  
  
exposuredetect tool is designed to cater to a wide range of users, including pentesters, security researchers, OSINT (Open-Source Intelligence) practitioners, and red teamers. Its versatility allows professionals from various security disciplines to utilize the tool effectively and efficiently in their respective fields.  
  
## Installation And Setup  

1. Clone the repository
```  
git clone https://github.com/leem4464/exposuredetect.git
```

2. Prepare and activate the virtual environment :  
```  
$ python3 -m venv myenv  
$ source myenv/bin/activate  
```  
  
  
3. Install requirements :  
```  
(myenv) $ pip install requirements.txt  
```  
  
To utilize the tool, it is essential to obtain an API key from CriminalIP. This key should be included in the script exposuredetect.py by opening it with your preferred editor and assigning it to the api_key variable in the 4th line .  
  
```  
api_key = "******YOUR_API_KEY_HERE*******"  
```  
  
## Usage  
  
  
  
### Get a list of supported products :  
```  
$ python3 exposuredetect.py -l  
```  
### Output :  
```  
(*) List of supported products :  
===============================  
elasticsearch  
mongodb  
couchdb  
laravel debug mode  
django debug mode  
kibana  
```  
  
### Get vulnerable IPs :  
```  
python3 exposuredetect.py -g "elasticsearch"  
```  
### Output :  
```  
198.177.125.113  
198.24.164.122  
198.24.164.123  
198.27.76.237  
198.27.77.221  
198.38.77.38  
198.45.114.169  
```  
  
  
## Add a specific product  
  
Suppose you're in search of Apache Kassandra, but unfortunately, it's not supported by the exposuredetect tool. No need to worry! Simply open the "exposuredetect" Python tool in your preferred text editor, and effortlessly incorporate your favorite product into the script.  
  
```  
...  
q = {  
"elasticsearch":"product:elasticsearch port:9200",  
"mongodb":"product:MongoDB",  
"couchdb":"product:couchdb",  
"laravel debug mode":"title:Whoops! There was an error",  
"django debug mode":"DisallowedHost at",  
"kibana":"product:kibana",  
"kassandra":"product:Cassandra port:9160" # new line added  
}  
...  
```  
demo:  
```  
python3 exposuredetect.py -g kassandra  
198.109.25.173  
198.109.25.230  
198.244.179.190  
198.58.118.130  
201.168.138.253  
202.109.248.196  
```  
  
## Disclaimer  
  
Please note that I am not responsible for any consequences or damages that may arise from the use of this tool. exposuredetect is intended for educational purposes only. It is crucial to use this tool responsibly and in compliance with applicable laws and regulations. Any actions taken based on the information obtained from this tool are solely the responsibility of the user. Always ensure you have proper authorization before conducting any security assessments or vulnerability scans .  
  
## Note  
For the tool to operate correctly, it relies on CriminalIP. If you encounter an error during execution, it indicates that you have exceeded the query limit associated with your key. For further details, visit [CriminalIP](https://www.criminalip.io/en/pricing)
