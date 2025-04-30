

class LinkVerification:

    def __init__(self, link):


        self.easy_check = False
        self.link = link
        self.PROTOCOLS = ("http", "https")
        self.TOP_LEVEL_DOMAIN_LIST = [".com", ".ru", ".org", ".net", ".io"]
        # self.ENDINGS = ("/", "//", "?", "!", "@")

    def get_protocol(self):
        link = self.link.strip()
        protocol = []
        try:
            for digits in link:
                if digits == ":":
                    break
                protocol.append(digits)

            if protocol != []:
                result_protocol = "".join(protocol)
                final = str(result_protocol)
                result = self.check_protocol(final)
                if result:
                    return final
                else:
                    print(f"{final} - bad protocol...")
                    return None

            else:
                self.easy_check_protocol()

        except Exception as e:
            print(f"Exception - {e}")

    def easy_check_protocol(self):
        protocol = None
        try:
            protocol = self.link[:len(self.PROTOCOLS[0])]
            if protocol == self.PROTOCOLS[0] or protocol == self.PROTOCOLS[1]:
                self.easy_check = True
                return protocol
            else:
                print("There is no protocol...")
                return None

        except Exception as e:
            print(f"Error occurred - {e}")
            return protocol


    def check_protocol(self, protocol):
        for prt in self.PROTOCOLS:
            if protocol == prt and protocol == "https":
                print("secured connection")
                return protocol
            elif protocol == prt and protocol == "http":
                print("not secured...")
                return protocol
            else:
                return None


    def get_after_domain(self):
        protocol_len = len(self.get_protocol())
        link_no_protocol = self.link[protocol_len + 3:]


    def get_website_domain(self):

        protocol_len = len(self.get_protocol())
        link_no_protocol = self.link[protocol_len+3:]
        return link_no_protocol

    def verify_link (self):
        if self.get_protocol() is not None:
            print("Legit protocol")








def main():
    verification = LinkVerification("http://vrii14.github.io/")
    verification.verify_link()

if __name__ == '__main__':
    main()