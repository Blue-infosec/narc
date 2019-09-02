from common import Modules, data_strings_wide, load_yara_rules, PEParseModule, ModuleMetadata, is_ip_or_domain
import pype32
import base64

class njRat(PEParseModule):
    def __init__(self):
        md = ModuleMetadata(
            module_name="njrat",
            bot_name="njRat",
            description="RAT",
            authors=["Brian Wallace (@botnet_hunter)", "Paul Melson (@pmelson)","Kevin Breen (code borrowed from RATdecoders project"],
            version="1.2.0",
            date="February 21, 2019",
            references=[]
        )
        PEParseModule.__init__(self, md)
        self.yara_rules = None


    def _generate_yara_rules(self):
        if self.yara_rules is None:
            self.yara_rules = load_yara_rules("njrat.yara")
        return self.yara_rules


    @staticmethod
    def _is_number(s):
        if s != s.strip():
            return False
        try:
            if int(s) < 65536:
                return True
            return False
        except KeyboardInterrupt:
            raise
        except:
            return False


    @staticmethod
    def _get_strings(pe, dir_type):
        string_list = []
        m = pe.ntHeaders.optionalHeader.dataDirectory[14].info
        for s in m.netMetaDataStreams[dir_type].info:
            for offset, value in s.iteritems():
                string_list.append(value)
        return string_list


    @staticmethod
    def _parse_config(string_list):
	    config_dict = {}
	    isbig = len(string_list)
	    if string_list[5] == '0.3.5':
	        config_dict["version"] = string_list[5]
	        config_dict["Domain"] = string_list[7]
	        config_dict["Port"] = string_list[8]
	    elif string_list[6] == '0.3.6':
	        config_dict["version"] = string_list[6]
	        config_dict["Domain"] = string_list[8]
	        config_dict["Port"] = string_list[9]
	    elif string_list[3] == '0.4.1a':
	        config_dict["version"] = string_list[3]
	        config_dict["Domain"] = string_list[8]
	        config_dict["Port"] = string_list[9]
	    elif string_list[2] == '0.5.0E':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[7]
	        config_dict["Port"] = string_list[8]
	    elif string_list[5] == '0.5.0E':
	        config_dict["version"] = string_list[5]
	        config_dict["Domain"] = string_list[8]
	        config_dict["Port"] = string_list[9]
	    elif string_list[2] == '0.6.4':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[6]
	        config_dict["Port"] = string_list[7]
	    elif string_list[2] == '0.7.1':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[7]
	        config_dict["Port"] = string_list[8]
	    elif string_list[2] == '0.7d':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[6]
	        config_dict["Port"] = string_list[7]
	    elif string_list[9] == '0.7d':
	        config_dict["version"] = string_list[9]
	        config_dict["Domain"] = string_list[4]
	        config_dict["Port"] = string_list[5]
	    elif string_list[10] == '0.7d':
	        config_dict["version"] = string_list[10]
	        config_dict["Domain"] = string_list[4]
	        config_dict["Port"] = string_list[6]
	    elif string_list[21] == '0.7d':
	        config_dict["version"] = string_list[21]
	        config_dict["Domain"] = string_list[15]
	        config_dict["Port"] = string_list[17]
	    elif string_list[12] == '0.7d' and string_list[83] == 'netsh firewall delete allowedprogram "':
	        config_dict["version"] = string_list[12]
	        config_dict["Domain"] = string_list[7]
	        config_dict["Port"] = string_list[8]
	    elif string_list[12] == '0.7d':
	        config_dict["version"] = string_list[12]
	        config_dict["Domain"] = string_list[6]
	        config_dict["Port"] = string_list[8]
	    elif string_list[28] == '0.7d':
	        config_dict["version"] = string_list[28]
	        config_dict["Domain"] = string_list[22]
	        config_dict["Port"] = string_list[24]
	    elif string_list[29] == '0.7d':
	        config_dict["version"] = string_list[29]
	        config_dict["Domain"] = string_list[22]
	        config_dict["Port"] = string_list[25]
	    elif string_list[24] == '0.7d' and string_list[25] == 'TGVHZW5kUmF0':
	        config_dict["version"] = string_list[24]
	        config_dict["Domain"] = base64.b64decode(string_list[18])
	        config_dict["Port"] = base64.b64decode(string_list[19])
	    elif string_list[9] == '0.11G':
	        config_dict["version"] = string_list[9]
	        config_dict["Domain"] = string_list[2].split(":")[0]
	        config_dict["Port"] = string_list[2].split(":")[1]
	    elif string_list[10] == '0.11G':
	        config_dict["version"] = string_list[10]
	        config_dict["Domain"] = string_list[2].split(":")[0]
	        config_dict["Port"] = string_list[2].split(":")[1]
	    elif string_list[10] == 'VISION':
	        config_dict["version"] = string_list[10]
	        config_dict["Domain"] = string_list[4]
	        config_dict["Port"] = string_list[6]
	    elif string_list[12] == 'im523':
	        config_dict["version"] = string_list[12]
	        config_dict["Domain"] = string_list[4]
	        config_dict["Port"] = string_list[7]
	    elif string_list[11] == 'im523':
	        config_dict["version"] = string_list[11]
	        config_dict["Domain"] = string_list[4]
	        config_dict["Port"] = string_list[6]
	    elif string_list[2] == 'Hallaj PRO Rat [Fixed]':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[6]
	        config_dict["Port"] = string_list[7]
	    elif string_list[2] == '#######Hallaj PRO Rat [Fixed v2]##########':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[5]
	        config_dict["Port"] = string_list[6]
	    elif string_list[2] == '0.8d':
	        config_dict["version"] = string_list[2]
	        config_dict["Domain"] = string_list[7]
	        config_dict["Port"] = string_list[8]
	    elif string_list[21] == u'\u1f70\u1f6e\u1f77\u1fa4' and string_list[22] == u'\u1fbc\u1f67\u1fbc\u1f67\u1fbc':
	        config_dict["version"] = '0.7d-HiDDen'
	        def hiddenperson_decode(cfgstr):
	            c = ''
	            for a in cfgstr:
	                b = ord(a) - 2 - 1
	                c = c + chr(b)
	            return c
	        config_dict["Domain"] = hiddenperson_decode(string_list[15])
	        config_dict["Port"] = hiddenperson_decode(string_list[17])
	    elif len(string_list) > 95:
	        if string_list[94] == '0.7d':
	            config_dict["version"] = string_list[94]
	            config_dict["Domain"] = string_list[91]
	            config_dict["Port"] = string_list[92]
	    elif string_list[4] == 'zwazwczwtzw' and string_list[47] == 'zwvzwnzw' and string_list[53] == 'nzwezwtzwszwh' and string_list[54] == 'fizwrzwezwwalzwl dzwezwlzwezwte azwllowedprogrzwam "':
	        config_dict["version"] = '0.7d-zwmod'
	        config_dict["Domain"] = string_list[83]
	        config_dict["Port"] = string_list[84]
	    elif string_list[25] == 'Eroor':
	        i=0
	        while i < len(string_list):
	            if len(string_list[i]) > 20:
	                try:
	                    domain = base64.b64decode(str(string_list[i].replace("FRANSESCO","M").replace("Strik","=")))
	                    if is_ip_or_domain(domain):
	                        config_dict["Domain"] = domain
	                        config_dict["version"] = '0.7d-BR'
	                except:
	                    pass
	            if len(string_list[i]) > 2 and len(string_list[i]) < 9:
	                try:
	                    port = base64.b64decode(str(string_list[i]))
	                    if njRat._is_number(port):
	                        config_dict["Port"] = port
	                except:
	                    pass
	            i+=1
	    elif isbig > 139:
	        i=0
	        while i < isbig:
	            if string_list[i] == '0.7.3':
	                config_dict["version"] = string_list[i]
	                config_dict["Port"] = string_list[i-3]
	                if string_list[i-4] == 'False' or string_list[i-4] == 'True':
	                    config_dict["Domain"] = string_list[i-5]
	                else:
	                    config_dict["Domain"] = string_list[i-4]
	            i+=1
	        if string_list[103] == '0.6.4':
	            config_dict["version"] = string_list[103]
	            config_dict["Domain"] = string_list[107]
	            config_dict["Port"] = string_list[108]
	    if len(config_dict) > 0:
	        return config_dict


    def get_bot_information(self, file_data):
        results = {}
        pe = pype32.PE(data=file_data)
        string_list = njRat._get_strings(pe, 2)
        config_dict = njRat._parse_config(string_list)
        if config_dict:
            domain = config_dict["Domain"]
            port = config_dict["Port"]
            results['c2_uri'] = "tcp://{0}:{1}".format(domain, port)
            results['version'] = config_dict["version"]
        return results


Modules.list.append(njRat())
