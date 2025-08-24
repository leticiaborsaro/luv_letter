import webview
import textwrap # clean up whitespace in python string

class API:
    def get_message(self):
        message = textwrap.dedent( '''My dear,\n
        You are very dear to me. \n
        I love you so. \n
                    Love,\n
                        Your darling''')
        return message.strip()

if __name__ == '__main__':
    api = API()
    webview.create_window("My Love <3", "index.html", js_api=api, width=800, height=600)
    webview.start()
