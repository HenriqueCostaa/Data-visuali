import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash_canvas
from dash_canvas import DashCanvas

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_daq as daq

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,'/assets/style.css'],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}], suppress_callback_exceptions=True
                )


server = app.server

filename = 'http://3.bp.blogspot.com/-OzrSP37BV4k/UcZevxNwxPI/AAAAAAAAYno/_7TQoKqCnAM/s640/Bowser_Artwork_-_Mario_&_Luigi_Dream_Team.png'
filename3 = 'https://2img.net/h/rockntech.com.br/wp-content/uploads/2013/12/mais-uma-teoria-maluca-sobre-pokemon_1-equipe-rocket.jpg'
filename1 = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBQVFBgVFRcZGRgaGx8fGxobGRsfIxwcHBsdISMbGxobIy0lIR0sIR8jJTclKi4xNjQ0GyM6Pzo1Pi0zNDEBCwsLEA8QGBISGjMhGiExMzMzMzM1NDMzMzMzNDE+MzMzMzEzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzMzQxMf/AABEIANEA8QMBIgACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAAABgQFBwMCCAH/xABJEAACAQIEAwUFBAcGBAQHAAABAhEAAwQSITEFQVEGImFxgRMykaGxB0LB8CNSYnKCktEUM0OisuGzwtLxFRdj0yQ0VHODk6P/xAAaAQEBAAMBAQAAAAAAAAAAAAAAAQIDBQQG/8QAIxEBAQACAgICAgMBAAAAAAAAAAECEQMhBDESUUFhBSJxE//aAAwDAQACEQMRAD8A2aiiigKKKKAooooCiiigKKKKAooooCivDMAJJgDcmqPG9rcHbn9KHPS2M3zHd+dBf0Ui3ftKwwOVVYtp3WYK2v7IBqwwXbfDuYcPb8SpIHmQPwoGmil3ifayzbHcBusRICbD95jt5CTS7d7Z4n9RFHkT6Ek0XTRKKQrHbm7960jeTFfrNWWG7aWyQLlq4niIYfgflQ0bKKgYLi1i7GS4pJ+6dG/laD8qn0QUUUUBRRRQFFFFAUUUUBRRRQFFFcnuqsZmAnQSQJPQTvQdaKKKAoryTG9JnGPtGwdi41sC5dZTBNpVKg9MzsoPQxOtA60VmWI+1cf4eFZv37oXTr3Uaq+59quJPu4e0vmzt9MtBrteGYASdAKxq59p+PJMLhwP3LhI9Tc/Cqfi/bLHYhcj3AFOhCKF6mZ1M6bzpyoNfx3a7B2nFs3c7nZbas58+4CI+lfuI7QSv6NTJ5vpHoDr8qwrAY25ZBFpsk7kKhJPUsQST51LbjuLP+M3wUfQUGicQd70m67Mv6s5VH8I0/GqbEvbBKWwuZYMAA77AE86TXx159GusZ6mv23ibonLdInfvdKTq7L3NHzAcJTN7RghuxBYQYHQfnWrlcKOYHqKzBb+IP8AjfFh+NXHALeMuXFVcSQJ176nYE7MI5UvZOj6nDrcRAnrXRcLbH3R8K8G1dWJKH1GvoD410uK6gloERznf1qaqomLw9gCSFB6x9aWeK8WtIrBRtzB0GvXmTyWmPiHBrl5YHmCATHjoaVeIdiLjEKboAWZBU+91Ou9NBbTibXLih2ZLZIkiM0E+9rKjyg+daRYxj2bYQO+QbFnY6fvMdP3dKzPi3B/YubefOQAZAy9dOelSMClw3bdpLjKRpmzR7ok6Ex10q6Rp2E4lctw1u4XX9V2LD56imfhvGEu6Huv+qef7p51lOCxNtrht5vZYgEQw0S7mAMMNQDqB16HlV9hcUWYo6FHA1Gbod1PNehHrUVpdFLPB+NxCXTp91yfkx/H49aZqqCiiigKKKKAooooCsY+166Hxlu23urbXfqzNJE+Ea+HhWz1Q9o+y2FxqxeQ5gIW4hyuvkdiPBgRrtQZd2Txj+1yviL6qgBtoL9wLObWVzQwEDukEa6jWnTE9oXj+9Pn3R8wBSL2i+znF4aXtTiLY1lARcUa72+enNSZ6CkpnOx16g9R+NBrtjiBxD5EJuuNSobMQOup0pE4n2axtu6ynDX2kyClt3BBJglkDAHqCZFLijUFZDDUdQRrII2q9wnariKZQmLudzUBzmB20bOCWHnQTcP2N4k22Ff+Jra/HO4Nesd2Mx1m2126ltFXSGuISSdgoUmSeQmta7MdpVxOCXEuAjKCtxdgHTeJ5HRgOjCk/ivE3x2I2K27fuIebEau0cwPrQIdnguJd8ioJiZkwPAkDepL9mL2cJntZge9DtCafeOWJjkJOvKr3ivExbtsLRIRffuDdjr3bZ+Mt6DqK7s1cuYnRECWwQC8GdTtJ33qbV3wnYPEvqbiKDtoxkdakf8Al7emP7Qk9AjH496nFMS0lVIhYGu2g/OlT3xNtBnIzMF5AzoJgQPxps0zbBdirtzFthVvKClsO7+zJCZmIRSubVmALb7Cr4/ZNd/+rT/9Df8AuUw/Z/ctmz/aGdDexTm44ze7Oip/CgA85p1LVUZI/wBlF8bYq2f/AMTD/nNR8R2GxGDHtxibcowAGR9S3dy6mOda+11QCen4UhdpsWb95LZbKg748SZVT+7o3xmgiOjDMSzgLqGOWIgEk6CPjXI3rh2cE+Whq1IA7m/Izz0rlf4ZMZMqjmNemmUDTzpsVWD4jed2tkhcqy2h56CNdZNWow9wkAuJIJ908on73jVe+FuscoEHmRHKYJ5xqausLaKtLkyE5kGSza+kgfKm6pV412auXbkrcXMQQQVI93mIJ+cUu8XwF/CXUuNlYTIcA5c3NWHL46/R/wCLcXTDJ7W4ubOYQDnppJ5aVXWcYcbcvWoU2kQShAADE833UCIB0151NjPb99rjM7ak/mPz0q+4T2hud23cD3I0Rl1ceGp73nM77iqLH4Y2rj2yGgHu5omNxMaTVp2Utg3mJ+7bYjzJC/Qmqhzw14sk7giVMRmHQjkwOhFMfZ/jWUi3cPdOik/dPQnp9Por2LkAyYA581M6Hx1Nfl8lmIJht/COsVFavRSt2W4wzRZumWjuN+sBup8QNfEeVNNVBRRRQFFFFAUUUUBS32i7GYPGS1xMtyNLtuFf1MQw8GBpkooMC7S/Z3jMLL219vbGue2DnUftW9/Vc3pS9w7EqsOYLg6yYkciPpX09SB2m+zzh9xnxTm7b3Z1tuArsT0ZWIJP6pG9BQ4niaJgra2znZlV3YbF3HdQH9VdvMVU8LW4F9hmlyZutMaHX2azsWkT0BXrpx4ms3LNhO6NT3SAQFGUADyPypmwHDFW4rAaBSIncsZLHxJqWrInYDhNt7fsriBl0YgSNST8okVx4riEwy5O7aQe4oGrHllQbjxPxqZxTia4RZbvXLmlu2NyR99hvk09fnVNY4KfaHEYuXd5bIT7o5AxtPQbCRzIoIKcRxJg21FtY0dwCfEgMNPh61PwvDGuy97EXH0EDOACWkjkeQJ9RU67YlpO+gG0QB02ipWGXKRzMFoM9ABqfAdOdBXJ2fw1u1OZlCSdG90CWPvAzAB5VG4PjMVbsJdS6yl+8EY93KzHIIjQ5YJ015V347ilNn2StrcYJIk+/odttJ+NSsXYUkALA5GR92FXnvppQSuFdrLdy6bd6EdWKE65SwMRB2M7cjUDtPh71y81+yHKlVUFRuwJ1HOPLfy1q29grWnt3BnVxBkanyI105GuXZnHHDXBhXYtaIiy7anTe2x6jly+lBTdmMPiyzHEpc3mXU/XY+lXd19Ryg8xTot9SuYGRVVxvEhrRCn3o66idflQKaAF+66qsHKNBAE6jnFRsZiyMSrMAy27Az6GQXbUheYOXcVZYTs8t1hclso1CbEEbanWOcVL/wDBAWNwghyTqDvpCghuQgfk0Fbx5LNwLcdJOUBQVnuuQDpsdDz21qs7N8OfBD2iKHuNMgTlKk+5J5f0Bpjx3C4tq2jOiwAYE9VhRGpJGlVb4K4QrISoaCOgURIHqCfUUFV2twVi4faQ6BlBdAAQja6KQCPHTx25KfZ697O+VfSVZZMeBE+OlOPaIvaVFKypbK7RABOx03G9QcR2et3mDLOaAdyAR5jw1FNizw1q3ctnUMCTMHeDEeUj5GuE9wKT3xtOkgAaMSN+XpVpheGi0FtgQFBPjtpkPly/aqn44SlxVg6gw3IQdFfo2p9aDx/bcrAhspGoIPusNefQ1pPZzjC4qyHEBwYdRyYdPAjUefUGsaxF1mAZhrJAjmRpmI/O1duy/adsFiO88oxAuJGkcjPJhM+vjVRvFFcbF5XUOhBVgCCOYNdqAooooCiiigKKKKApK7XcatuFtW3VwGJuZSCBlGxI+nlTJxzFeyw9xwYIUhT0Zu6v+YisttWFUhQe7BYsf1Rlkn0HyoInCcIr4xr5klO6AdgBPzkn4U7cKVWL3HnIh1H6zToB6/SqDBWltC5cHJZ/euXIC+UAAx+0a8niJypgk7zOC1xuhYwT49zTwnwqMltwnD/2nENi7msD9HO2h94DkOQ8us1NxpJJjqB6D/evaX0tAjMiKAAAzgEADn41VYjj2FUicRanoHBkmNND5VWLriMwUnUjwgGYnwqo4pj/AGarcZ8od8iSSoGUBiWbeIAED3s0dY/cT2qwmZVuXkC8+6YPKJ109KLfF8FcBBuowmQvsrjQf5SP+1Jjb6hbIrkecRYVQcjO91c06hLcg/zGfhTlZwsCTl0jbppSYvGAccLkNkt2iiNkeCzky0biAY1pww/H7GUZnTxzgjXrqRWV4857lT5438re8gyT01+H/alPjA/Rlc2qZSD+qykGR46H51c4ntDh8hAew+moW4ARJ/en4VX4i9burpGpGgf1Py+tSyrtO4Vxk3ERz3WbuvvqV7p05bSK7MZdhJygTGviZ1paRGt33t5WysUuKBB0IKtlPmAfWpOC4sodnYsBrmBElee1Yqb8D3RBJMtGqgRK5uXKIruqKdTrDAjwkco8DVF2e4u92zhsy5WuO/uqSCgRyGJMxHd1nXQc6Z0WGA8fwoOXFba5JOmo1mNAZPyFVN/CWrg9mw0A2E9dNRttV7fMkI0SQTHhtp8aiNhhnBj5eQoK7HYVMgVu8oImdT0338aosZ2cQiUZ0IjKV5HYEjmOvWmLH8PAYXEbKZgiAQ40GUg678xtURMSpz5WErKg9G2Ig7n+lBwwmHuphs9xxcIYhSu7D7vqOfWBSvx1jlIO5MHxJ2g786ceOXghS0GAKCT4uR9Y1/ipMx7F7gB+6C7eJXp6kURR426tpHuHZFgDqRoB6nSkHh+IJc5jJYkk9Sd6Zu2d/LbS2Jl2k+S8viwPpSbhWh184+OlUfRH2TcV9phWsse9ZbT9x5I+YNP1Yp9kuLK4zJOly2yx4rDA/AH41tdAUUUUBRRRQFFFFBT9p8KtzC3FYkCMwIjdSCN+U1nWPtFWS2F0uEAeCrJM+ZIEdDWkdoWPsGA+8VHzn8KRuIBDisqgZkVQGMHurM5TuAXMN1KL0FBwxRm2BsHvf5bc6/BKUjdJV7kQ1xgFIMHeRqP2WI/hpqvLFu3+xZuNr1CL/U0r3xpZUaiTr+4WAPwqLVT2nuKrMFAAVVTTq4LuT5qEE+NVODtQ37g//o3P+HU+VsV342+e4AdnuvPkHCD/ACp865Wn/Ru/Ni59YAH+s1URCPaXIHuiAB4Db8+NOHC8JAAH4Utdn7OZ/M1onZ/BszDulvLwHhXX8LDHHC5VzvM5LJdJmG4coHemen9akjAZu7kOuwHP4UxcJ4Xn1bTXp4bVf28OiEtu0QCdwANh8K18vlX5dNHB4luPzzvdZpf4Oqq5Ze/pBBBAUDYxudPzvSrjsIFLQBp5enjyrRuMqPaNoNAZ0386QuJ+82k8p6fnWut4398O/p4+LPL/AL5TfUSew6G5iQrMfdZZJOnPSfL5U1YvhgW4c2UrI+A23586VewFhnxUAaAMT5KPh0+NaNjy1237MbnqIMHTevm/IxmPJlJ9vouO7xjl2YvNbdrJJKHW2SD3Cd08juOhkcwAxs3eU6Qp+EiKpcLhoVipEqhjcw2g1B2O/wBaseCY1byZtC05X8GAEiPWfWtLNY3Ukg6afQ7j5VzYd4eR+oqUBXMjvDyP1WiIWJsK3vDQEHXqNRUHE4NGAUrmBcEjrl1389PWrx0B32qItgEGAVEQNNvTkf6UUlcawxu+12KvqAxPdJmV0Eg/18KW7JKs/TKFGYyRLExm56Aa0+8Zw+Ve5qengDqNaRsY3vnmXPpoB8qRFL9oOBH/AIbg7/W9dH8+3/CrNAYaehpr4zxa7dVsKzn2WeUQ6hWTOMwnVZzMNNNdaU23NUaZ9nV8Jj7B6sV/mUj8a36vm/sbdC4zCt/6if6l/rX0hQFFFFAUUUUBRRRQV3GBKoImXX4AE/hWfqmbHCNnt5vVrlwn6itFxxANsnYOf+G9ZYmLdbli5bjM1oASJEaTP84oLjiULmaNrV1Rt+qR8ZFJRbM9kjSc8eZzEetXXazi9xbtm0QgDKCxAgtJOYASY/EmpPYq6q3HtiCCAe8AfdMQJ121pfZPTMOKkC4mo/vbnyvmuS/3BH73y9nX0O/CrRSfZ2Tz1tz+NL+H4ZhnkGxaMs26D88vpQY52fePj4fjWhcIeCp16E0xWOz+EDHLhrW/JVH/AC1Mv8GtBdLYWdZVoy+Pu17+DzMcMPjY8Xk+LlyyyXWxheKNZUiZLHaTK90y3SNq83OMOYj+sz1qmwGHFxrwa5mKXRbVy529lbYRpzLEz18hTIvZ0KoZmkRJhj+I2pj5HBPeN20cnjeRcZjjlCzxLHhVJJ1Om/4j1pMxd897XffxrQ+K8Gw0ZitzT9skfWqK72bsthLmIYsMkkKGGuoAWJ3JI+Ne7D+S4ccLMZdsfH/j8uPvKy2vX2Y2+/cfKTIy7ka5gSAepCj0p6xmCzBUts2e4wBZjqqgSzCOg0E8yBS/2Zs+xspZXu3Jz3JBGuUFVBjltrzUGrbgOMNxHuqrMDmtWiBowUnPczDkXGWeYtqRvXD5M/nncvt1pNSRMw5S3Yusmudiqga97Xaemp9DVR2fJw+LKZpS5CsNdHAlW1O8krA/WHSm3BYBLdtbYA01E6w3X40p8cw+V4CZCbigOGOuUZ2aJ0Og2jesVPLA8q5s/eUdQ3yivOEvZ0VuoE+fP50OxlTHX6f7UR3muKCf6V7W4DEGZr9ziJmqKTjqd0TH+1ZxiTIY9XaP5iP6VoPaG0zrAYDUEyOQOwPInrr5VnTv3VHT6yTQZ5i7a3LjMrKWzEjXKd+jQD6E1W4nCMCeu5XYiek8q7nBvyZW9YJ9GipOEQZHW4xBUEqraEabgnUf7UFx2T/+Zwv/ANy3/rWvpavnHsYpOMwo/wDUT/UK+jqAooooCiiigKKKKCv4xYL2wAYOYa+YI/Gsg4dfjDYW4T/dnI59Cp/zqBW04j3SekH+Uz+FYpgrA9rxDAt929cKDorMWQ/HWgmdpcLdu27d22mYhsyKIzHKD3gDvJkAdAPSJbuPYe3fUDKYBjaI92Y5pr6Uz8LxS3LQaCsSoA/wwFgEdCq7+Nc+H9iytu7ba4XVzmnLGWFEESTLSJnTeKButX1eyGUypEg+BFLGDukiQdFYg1ScI4rcwhfCXz3J7jAyFnmD+ofiDUnht8qHBP3zpy23qKvrGIBLTIJIjz2+FSr7koZIJIO/TaKpElm3FTWzFUnlp/Q/KiOGDsC0bgC6O4Ya9EC/hVymKLCOUD5AVTNcltN4M+gH59alhyoH55UVIx+CFy2RJBnkfyKXuyvDHvXhmM2Lbgt0dk2XXcKdT4xXW/xG5eJtWToT37g+71C9X18hVjf4pbwWGyiFVBJPQDqepPxJoOvbTikqMNZJ/tGKItWhrKK3v3jGoVVn4edM/CuF2sPZSzaAVUAAgdAAT5kiSetZv9maPjMXe4pfU6k27AIMKADJXlovdnq71rNVFNiLeMUlle0wjQFGU+sE0r4/HXLl1mulALIKjLOWTBcyegAHxpr45xIWbZI1Y6KOrHQD89Kyft1xL2GE9kG/SXZBPgTLt+HrUU+/Znxz+14Rm5peuL/CWzr6ZWA9Kab5AKn9r6qRWXfYVK2sQp0zFHA6A51+ig+tanfWR6j6j8KqPaKBsIqLeGSAPQetSVmdelcsSgJE8qgTeOW2W4TnYwDC8pO7HqdKQGukL6T6/k1o/aSyNCAeYmeUVmjpymBER61Qh27gyZIOfOO9OmXYiOs868HE5lyEacjvHlO1TeKYE23ck7Tp0Y6eUayPOqmwJdR+0PrQaL9n1vNxDDjo0/AE19A1hv2WYfPj0aNEV2/ylfqwrcqAooooCiiigKKKKD8IrDu33/wXGExGyX0XOeWZe43wyqx8zW5Vm320cE9tghfUS1hs233GhW9Jyt5KaCJw1hbu5f8ADuEuvQN99f4hr6t0p6fFJbtszbBSfQCsc7E8VF+x7G4e/bgBucD3W9NvH1NMmJ4zce6mHfSZDL+soynMOqwCPXWgtbfAhesg3EBZu8SNGVjqSp8yfDzpbdLuDdgsXUnVNAy6RsNQfESPCtPw3uCOlLvGOD27lz2j5QdAGaNNdoIiT1magW8Nx6yT3iUP7akfMfjFTX41YIX9Im0iGGvhp61YdpOzC3MJcK6uttmQ+IUmNOR29a48Ls4NcFYv3VVUa2nvE6FlACgDczpAk0VU3+NWwf0StcLHYKdzyBO1W2F4LjcVHth7C3GqDQsOhO8eUVYcC4tgnurbsBdsxbKywFaNmAMeNOD92T+daBeTCWcOoUQsDu7DXypM7W8Ju8QOHt2iBZknEXZAJyscqhNzAmNIJI6aTeMYe5cvsLkQGbLIiRpt6R86uOCYkAZSqjJ06TIOm28elAx8F4etq2qIoRFUKijko2nxO58SalYnEBQROsfDxqFf4qAvcgnkP60rY/iT3Ztg9z77D737I+hNERMZjQztdZjkQHKWOnOX1+VZFxfGtjcS9z7iDQfsA6epOtW/brtCHJw1k9xT32GzH9UeA50vdnn77jqp+RH9amV1Lasm+mqfZDeAv3wTH6NYH8VanexK7c4mKy37KuHB7mIbKIVEAJ17zM5+WX5itSNhRvqfHw8KY5TKbno1p0S5MQPOo2LBLIwOgmfGpBaAI5Cq+9cbLPTb4VUUPay8yoACdSTIHyBpBs2tJbrHwNaLjjKHNOo0Hn4UiOkB05q5+Bg/jSDNuIMQhndnPwBP4AVB4es3B4San9pWi8yjkSf5jNceD25JPp+JqjYvscwffvXeiKnqxzH5KK1ak37MMGUwQYiDcdm9NFH0NOVAUUUUBRRRQFFFFAVFx2FS7be3cGZHVlZeqsCCPgalUUHzK9m5w3G3bZGYarJOXMuhVpiJIIMbSSOVPmBxFu6UZozocyP0kbeKMDqPxqz+1bsv7a0cVbWXtjvQJLWxqfMqSWHgXHSkfsnigyqp5GNBGmpEdRuPQUGn4XjOVsjiBIynqCPnr9aMcc5QqxHeIYSdRm8iCIPzqkdCqgMMybg9D18D41+WcQ6SVY+8GkeUQRsQRQP+DIKZTBER5isn4LZuW8OysjXFwmKMWwQS4RnDKVbwKsBoJX43+D7QOl1kIIQqCrxoGkyp5Dr/AN6h8LxWXFYq2RIdlur451AY/wAwoPWH4jbxOMw1ywjKyBzed7TJlSFm27QCdW01KkqYG0aPYxCkZW3k78+dJlvFW00DADkJ28AK6DjKxvJnTSeXyqCR25wRFn2qam22Y6/d5g9dPpS52Y47bZnzwpYZhHMCBFW9/izuCsZgeR22jUVR2cLbtbKJJ2GpP4ny28KCdibpuMSpKp8z/tSZ2v7QlUNmySq7M4/0oevU8qvuIXmIIaQsSQN/U/0pD7WpnZFtq36MZW7pjYMCCBGxn1pBDsdnbrKGBEx9daMFbNi4A4EEHUdDpOvx9KeOzHEkFhMyKYULJJnuaSdPClvtRirdxlW2nfBJ010J0WOZivNM8rZjZ73v/Pw2WTuz9NV+yeyEw9xz9+53T1VFAn4lqeRuT1pd7O4A4fB2cOQAyWxn/fPef/MTVt/aiBAAnnNb8ZMZJGFSLzaVXYm8ApnYak+Vc8SWLEliRGizAHia4MkNm10ERm7onckczy1+Ws5CnsYp7oZmGVPujWSD50u8RUB2E6lQdOcEg/Iir/H3LrXlS37i+8SPeJ2UHYL8z4CZq+L4LKyXZJyAyv7J97zPTyojKu1uGK3Q0aMI9V/2IqTwDh7uyW0Eu5AA8Sfz8KYeLYa3cGViABDK3SNj4iKevs47GmyRir05oPs1IiARGYg7abD16VQ/cOwgtWktrsiqvwETUuiigKKKKAooooCs9+1rily1YtJbd0LsxJRipIQDTMpmJYH0rQqp+O9nsNjAq4hM+WcpDMpExOqEaGBoelBivC7GLvXPZrisQCASSb1w7QNBm6mp+K7OY4bYq6w/auXP+o08/wDlvYR89jEYm00RoyOIPXOhJ5bnlXm72U4gnuYy1cHIXcPl+L22/Cgz7AYHiOHupdR8+U6qXYhlI1BDdR+FU190s4y41pctssYRR7mxyr3o0b6RWjcRwnFbKl3w9q8q6n2Fxy0eCMknrAk+dIOD4Li8Rna3hrzBT3pUrBJOnejMeoG3OKBt4b2vwxRRdZkYDXuMR6ZQanrxHBXD3MQik/tBf8rx+FZxicNctHLcR0baHRkM+GYCa4aGpoahieHOyEIUcERmVvyPnVDgbPsrvs7hYvlAVTBy6+6pHLXryEUnWxlMqSp6qSPmK7rjLoLfpHOZQCWYsYBMAFpI57das/Zf00VMLr/duf4TUhMJc+7bI8WgfjNI+H7W41P8QP8Avoh+agH51Ps9vcWPeSyw/dcH45/wqKc14Rcb33Cjokz8amW+FW0HdUT1OpPrSfY+0Vh7+GXzW4R8ih+tT7X2h4YnvW7ydTCMPk0/KnY78SwoUNoSI86zzjdg5wVzw6Ro+WChjY6E5SPhT9iu1+CuKctwho0Do4188sfOk3jFtblt3GVgO+DGYQNGAHXL9KIWExVxEZBIEzrvy5g7Uw9gOHG9i1uMBkt98yNGuD3AesEZv4PGqFcBce4tu2hLPsAjL4yZ0AAnWtGwmA/sthEtjMVYF2Gkkxmbr5eAFBoL3+8ROv06fSuOaCJJA89vPrvVGuNDALrsPvHNy1/PWptkmIbQctuZMa0Va4owdNq8JZzrGmv5/PnUi3aERMiNNede7YCU0OK4EAyeu3TSq3juGGUsBRjO0dvOVRlOX34Mx/WjhRfGawUtzvzj/qPTkN9dKCF2U7Mo7+3uJ3VPcU7Fp3joD8/KtArlatqihVEACAOgFdaqCiiigKKKKAooooCiiigKKKKAooooKLtL2ZsY23kujX7rAwVI2II5j+vIkHKuK8Iv4NymJttdtD3MQtvNA/bAB+I66gVuVeSJ0NBg5wlh1BCIQdipIkdRlMVW4rBW01KOF2zIwaPFg4GnlNbhiuy2EfMfYqjNuyDKZ66aE+YNKXFexLrOX9Inho3qvP0+AqKyTDX1ZyjMEgkZiOQ2JG4mphROV+wfO4Afgamcc7MZTmtSGXbTVf2WHT6UsYgMpy3FKkbHl5BunODWWk39mUcOvwCLeZdwVKNM8xlM1ye2y+/aYeasPnFd+zHFM0WnIzfcOne8J6005juZ8NdvSsdrITrT2Ce8GA11BB5VpWH4bgntrkIAKgDQHQiDqDrpVMLNtjDopnqoPxmrFrqsoQGANhC/COlNmnfDdlrVvv2Sqtl1gkHTkAwj4V2Tgt3dYadYMGfgaV+JpeQH2dx0OuUhiN+R5Eac9vI1y4H2nvhvZ37hZuRhdY6iKu4hixGBuhwcsFZB1I0O4gjwHwqBj+1Psn9kbTMRuQ6gyY7oBBBB8xH0tE4i76yJ6Eb+Milbi/DLrX/aKFZWZSYZRAgA+8R506FliO318MyWLKGASGfMxyj7xRSI+Jqg4l2uxt9cr3MqndbahQfXVo9a8YDFCw10uh1SASp0ytJg8gdp2iqUHQc6Bv7F8IRntO5ILuRI/VkrGvU/hW04ewqKFQAKNgKzTsRYzthY2VMx/hzGT/FHxrUaAooooCiiigKKKKAooooCiiigKKKKAooooCiiigKKKKCHi8Baue+it4xr6Ea0u8T7C4e6DBKk8yFb+nzpuooELA/Zjg0cO5Z4MwFVQSOpAn4EVZ8V7Myc1mIj3GJ3/ZY/Q/GmmihOmWYvhV1Zm248wY9Dsa4pwu5uEufwo5+grWqKml2zSzwTFXVC+zZR1cZT8GivJ+zZmObOqN+se8R4bbetabRTRtkbdkuJ23jItxQdGR0AI6EOVPyq/wCGdjLrw2IZUHNLYlvIue6PQHzp9oqoiYHAW7S5bahRz5k+ZOpqPjeBYW7PtLFpieZRZ9GiRVnRQLvZvstawRYpcuPIhQ5XurMkDKomTuT0G2ssVFFAUUUUBRRRQFFFFAUUUUBRRRQFFFFAUUUUBRRRQFFFFAUUUUBRRRQFFFFAUUUUBRRRQFFFFAUUUUBRRRQFFFFAUUUUH//Z'
filename2 = 'https://media.pocketgamer.com/artwork/na-uzant/kefka.jpg'


canvas_width = 300
canvas_width1 = 300
canvas_width2 = 300
canvas_width3 = 300

# Dataset Processing 1 figura



df = pd.read_csv("Evolution_Videogames.csv", sep=";")
df.rename(columns={"x": "run"}, inplace=True)

# dataset processing 2 figura







df_consoles = pd.read_csv('vgsales_2019.csv',sep=",")
df_consoles = df_consoles[['Name', 'Year', 'Platform', 'Developer', 'Genre', 'Critic_Score']]
#all data from 2020 is wrong, i'm eliminating them here
np.where(df_consoles['Year'] == 2020.0, df_consoles['Year'], 1976)
#same with data <1977
df_consoles = df_consoles[df_consoles['Year']>=1977]
#merges global sales and total shipped, it's the same thing and they complement each other
#df_consoles['Global_Sales'].update(df_consoles['Total_Shipped'])
#del df_consoles['Total_Shipped']
df_consoles.rename(columns= {'Critic_Score': 'Score'}, inplace = True) #renames column


#data para a 3 figura
df1 = pd.read_csv('use_on_racing.csv')

dict_keys = list(range(1977, 2021))

years = list((range(1977, 2021)))

n_frame = {}

# set base case
dataframe = pd.DataFrame(columns=df1.columns)

for y, d in zip(years, dict_keys):
    # get list of games published in year
    dataframe = dataframe.append(df1[(df1['Year'] == y)])
    dataframe = dataframe.nlargest(n=15, columns=['Total'])
    dataframe = dataframe.sort_values(by=['Total'], ascending='False')

    n_frame[d] = dataframe

#print(n_frame)


####FONTES
def_font= "Bahnschrift"
title_font= "Cooper"


#### COLORS
color_box = '#457b9d'
back_color = '#1d3557'
shadow='2px 5px 5px 1px #6930c3'
shadow2='2px 5px 5px 1px #ffb703'
# ------------------------------------------------------------------------------

#figura 1 construção grafico


# Base plot
fig = go.Figure(
    layout=go.Layout(
        font=dict(family=def_font, size=18),
        updatemenus=[dict(type="buttons", direction="right", x=1, y=1.16), ],
        xaxis=dict(range=[1970, 2022],
                   autorange=False, tickwidth=2,
                   title_text="Year"),
        yaxis=dict(range=[1, 1],
                   autorange=False, ),
        title={'text': "Check some facts about video games that will make you feel nostalgic & old",
               'font': {'color': '#ffb703', 'family': def_font, 'size': 24}},
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    ))

# Add traces
init = 1
y = 1

fig.add_trace(
    go.Scatter(x=df.Year[:init],
               y=df.Released[:init],
               name="",
               visible=True,
               hovertext=df['Fact'],
               hoverlabel=dict(font=dict(family= title_font, size=15)),
               hovertemplate='%{hovertext}<br>Year: %{x:} ',
               mode='lines+markers',
               line=dict(color='darkcyan', width=18),
               marker=dict(symbol="circle",
                           color='#ffb703', size=10,
                           line=dict(color='khaki', width=4),
                           )))

##### ANOTATIONS
fig.add_annotation(
    x=1972,
    y=y,
    xref="x",
    yref="y",
    text="First Video Game!",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=30,
    ay=-90,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#ff7f0e",
    opacity=0.8
)

##### ANOTATION Pac-Man
fig.add_annotation(
    x=1980,
    y=y,
    xref="x",
    yref="y",
    text="Pac-Man",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-10,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#00afb9",
    opacity=0.8
)

##### ANOTATION Mario

fig.add_annotation(
    x=1983,
    y=y,
    xref="x",
    yref="y",
    text="Mario Bros.",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-30,
    ay=50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#90be6d",
    opacity=0.8
)

##### ANOTATION Tetris

fig.add_annotation(
    x=1984,
    y=y,
    xref="x",
    yref="y",
    text="Tetris",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=40,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="Gold",
    opacity=0.8
)

##### ANOTATION Gameboy

fig.add_annotation(
    x=1989,
    y=y,
    xref="x",
    yref="y",
    text="GameBoy",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=30,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="Crimson",
    opacity=0.8
)

##### ANOTATION Playstation

fig.add_annotation(
    x=1995,
    y=y,
    xref="x",
    yref="y",
    text="Playstation",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-50,
    ay=50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="#7209b7",
    opacity=0.8
)

##### ANOTATION Pokemon

fig.add_annotation(
    x=1996,
    y=y,
    xref="x",
    yref="y",
    text="Pokémon",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="DodgerBlue",
    opacity=0.8
)

##### ANOTATION Minecraft

fig.add_annotation(
    x=2003,
    y=y,
    xref="x",
    yref="y",
    text="Steam",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="slategray",
    opacity=0.8
)

##### ANOTATION Minecraft

fig.add_annotation(
    x=2006,
    y=y,
    xref="x",
    yref="y",
    text="Wii",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=-30,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="orange",
    opacity=0.8
)

##### ANOTATION Minecraft

fig.add_annotation(
    x=2010,
    y=y,
    xref="x",
    yref="y",
    text="Minecraft",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="sienna",
    opacity=0.8
)

##### ANOTATION Switch

fig.add_annotation(
    x=2016,
    y=y,
    xref="x",
    yref="y",
    text="Switch",
    showarrow=True,
    font=dict(
        family=def_font,
        size=18,
        color="#ffffff"
    ),
    align="center",
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="#636363",
    ax=50,
    ay=-50,
    bordercolor="#c7c7c7",
    borderwidth=0,
    borderpad=4,
    bgcolor="hotpink",
    opacity=0.8
)

# Animation
fig.update(frames=[
    go.Frame(
        data=
        go.Scatter(x=df.Year[:k], y=df.Released[:k]), ) for k in range(init, len(df) + 1)])

# hide y ticks!
fig.update_layout(

    xaxis=dict(
        # autorange=True,
        showgrid=False,
        tickmode="array",
        tickvals=[i for i in range(1970, 2021, 5)],
        # ticks=range(1970,2020,5),
        # showticklabels=False
    ),

    yaxis=dict(
        autorange=True,
        showgrid=False,
        ticks='',
        showticklabels=False
    )
)

# Buttons
fig.update_layout(
    font_family= title_font,
    updatemenus=[
        dict(
            buttons=list([
                dict(label="START!",
                     method="animate",
                     args=[None, {"frame": {"duration": 1000, "redraw": True},
                                  "fromcurrent": False,
                                  "transition": {"duration": 2000},
                                  "mode": "line+markers"}]),
                dict(label="FULL",
                     method="animate",
                     args=[None, {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate", "transition": {"duration": 0}}])

            ]))])
####
fig_layout_defaults = dict(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)', )



# figura 3 construção gráfico

# -------------------------------------------
fig_2 = go.Figure(
    data=[go.Bar(
        x=n_frame[1977]['Total'],
        y=n_frame[1977]['Name'], orientation='h',
        text=n_frame[1977]['Name'],
        textposition='auto', textfont = dict(family=def_font, size = 18),
        width=0.9, marker=dict(color =n_frame[1977]['Color'])
    )
    ],

    layout=go.Layout(
        font=dict( family=def_font, size=18),
        xaxis=dict(range=[0, max(n_frame[1977]['Total']) + 1], autorange=False,
                   title=dict(text='Global Sales (Millions of Units)', font=dict(family=def_font, size=18,color= '#ffb703'))),
        yaxis=dict(range=[-0.5, len(n_frame[1977]['Name'])], autorange=False, visible=False, showticklabels=False),
        title=dict(text='Top 15: 1977',
                   font=dict(family=def_font, size=32,color= '#ffb703'),
                   x=0.5, xanchor='center')
        ,

        # transparent color
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        # Add button

        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          # https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
                          args=[None,
                                {"frame": {"duration": 1000, "redraw": True},
                                 "transition": {"duration": 300,
                                                "easing": "linear"}}]
                          ),
                     dict(label='Full',
                          method='animate',
                          args=[None, {'frame': {'duration': 0, 'redraw': False},
                                       'mode': 'immediate',
                                       'transition': {'duration': 0}}]
                          ),
                     dict()]
        )]),
    frames=[
        go.Frame(
            layout=go.Layout(
                xaxis=dict(range=[0, max(value['Total'] + 1)], autorange=False),
                yaxis=dict(range=[-0.5, len(value)], autorange=False, visible=False, showticklabels=False),
                title=dict(text='Top 15 ' + str(key),
                           font=dict(family= def_font, size=32,color= '#ffb703'))
            ),
            data=[
                go.Bar(x=value['Total'], y=value['Name'],
                       orientation='h', text=value['Name'],
                       textposition='auto', textfont= dict(family=def_font, size = 18),
                       marker=dict(color =value['Color'])
                       )]
        )
        for key, value in n_frame.items()
    ]

)
# -------------------------------------------
# ------------------------------------------------------------------------------
# App layout

# figura 1

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'backgroundColor': back_color,
          'font-family': def_font,
          'font-size': 18})

page_1_layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.Button(dcc.Link('Go to credits', href='/page-2' )),
                        html.H1('GAME ON!', style={'text-align': 'center', 'color': "#ffb703",
                                                                    'font-family': title_font,
                                                                    'font-size': 55}),

                          html.H1("Timeline of Video Games", style={'text-align': 'center', 'color': "#ffb703",
                                                                    'font-family': title_font,
                                                                    'font-size': 40
}),
                          ])
                )]),

    #### GRAPH
    dbc.Row([
        dbc.Col([dcc.Graph(id='my_line_chart', figure=fig)],
                style={'width': "30", "margin": "20px", "background-color": color_box,
                       'box-shadow': shadow,'border-style': 'outset', 'border-color': '#80ffdb',
                       'font-family': def_font, 'font-size' : 18, 'border-width': '4px',
                       "display": "incline-block"}, width={'size': 8, 'offset': 0, 'order': 1},),

        dbc.Col([html.P('If your mother taught you that you should not spend all those hours playing video games, we have got good news for you: The World Health Organization (WHO) endorsed video games as a social activity to help spreading COVID-19 during the pandemic. This fact was our motivation to create an informative dashboard about video games. Today’s young adults lived through the golden age of video games during their childhood. Thus, with this work, we want to take you on a trip to the past and remember some of the video games that were part of your childhood, as well as some facts you may have missed about them.', style={'color': "#FFFFFF"})
                 ], style={'width': "30", "margin": "20px", "background-color": color_box ,
                           'box-shadow': shadow2,'border-style': 'outset', 'border-color': '#80ffdb',
                           'font-family':def_font, 'font-size' : 20, 'border-width': '4px',
                           "display": "incline-block"}, width={'size': 3, 'offset': 0, 'order': 2})

    ], no_gutters=True, justify='start'),






## figura 2
# App layout

    dbc.Row([
        dbc.Col([html.H1("Games from A to Zelda", style={'font-family': title_font,
                           'font-size': 55,'text-align': 'center', 'color': "#ffb703"}),

                 ])]),

    ###YEAR SLIDER
    dbc.Row([
        dbc.Col([html.Div(["Filter by Year(s): ",
                           dcc.RangeSlider(id='my_slider', min=min(df_consoles['Year']), max=max(df_consoles['Year']),
                                           step=1,

                                           value=[int(min(df_consoles['Year'])), int(max(df_consoles['Year']))],
                                           marks={i: {'label': str(i)} for i in list(int(i) for i in list(
                                               x for x in set(df_consoles['Year'].to_list()) if x == x)
                                                #,'style':{'color':the_color_you_want} for h in range(0, 24)

                                                                                     )},



                                           included=True),
                           ], style={'color': "#ffb703"}),
                 # , style={"display": "grid", "grid-template-columns": "10% 50% 100%"}), #play with slider length
                 ])
    ]),

    html.Br(),

    ###INPUT BOX

    dbc.Row([



        dbc.Col(

            [ html.Br(),

                html.Div(["Find Your Favorite VideoGame: ",
                           dcc.Input(id='game_input', value='', type='text', placeholder='Insert Video Game...',
                                     size='30'), ], style={'color': "#FFFFFF", 'font-family': def_font, 'font-size' : 18}),

                 html.Br(),

                 ##### TABLE
                 html.Div(

                     dash_table.DataTable(
                         id='table',
                         columns=[{"name": i, "id": i} for i in df_consoles.columns],
                         # fixed dimensions in each column (optimized to maximize width of column name)
                         style_cell_conditional=[
                             {'if': {'column_id': 'Year'},
                              'width': '60px'},
                             {'if': {'column_id': 'Platform'},
                              'width': '100px'},
                             {'if': {'column_id': 'Genre'},
                              'width': '90px'},
                             {'if': {'column_id': 'Name'},
                              'width': '150px'},
                             {'if': {'column_id': 'Score'},
                              'width': '90px'},
                            {'if': {'column_id': 'Developer'},
                              'width': '90px'},
                         ],
                         data=df_consoles.to_dict('records'),
                         fixed_columns={'headers': True, 'data': 1},
                         fixed_rows={'headers': True},
                         style_cell={'overflow': 'hidden', 'textOverflow': 'ellipsis', 'maxWidth': 0,
                                     ## esconde cels que tenham muito texto
                                     'backgroundColor': '#fca311','opacity':0.8, 'fontWeight': 'bold', 'color': 'black', 'textAlign':'center'},



                         # tooltip_data=[
                         # {"Console": {'value': 'The shipment is {}'.format(
                         # '![Markdown Logo is here.](https://media.giphy.com/media/1xjX6EOQZnS5ouhU5k/giphy.gif)'
                         # if row['Console']==['DVD Kids']
                         # else '![Markdown Logo is here.](https://media.giphy.com/media/7SIdExk63rTPXhbbbt/giphy.gif)'),
                         # 'type': 'markdown'}       }
                         # for row in df_consoles.to_dict('records')],

                         css=[{
                             'selector': '.dash-table-tooltip',
                             'rule': 'background-color: gray; font-family: monospace'}],  ### cor da legenda adicional
                         tooltip_delay=0,
                         tooltip_duration=None,
                         style_table={'minWidth': '100%'},  ### dimensão da tabela
                         style_header={'backgroundColor': '#7209b7','opacity':0.8, 'fontWeight': 'bold', 'color': 'white'},
                         ##header
                         style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': '#fb8500'}]
                         ### linhas listradas
                     )
                 )], style={'width': "30", "margin": "20px",'box-shadow': shadow, "background-color": color_box,
                        'border-style': 'outset', 'border-color': '#80ffdb', 'border-width': '4px',
                            "display": "incline-block"}, width={'size': 8, 'offset': 0, 'order': 1}),

        dbc.Col([html.Div(children=[
            html.Iframe(
                id='movie_player',
                src="https://giphy.com/embed/x2woMnCz4W0Vy",
                width="100%",
                height="600",

            ),
        ])

        ], style={'width': "30", "margin": "20px",
                  'box-shadow': shadow2, "background-color": color_box,
                        'border-style': 'outset', 'border-color': '#80ffdb', 'border-width': '4px',
                  "display": "incline-block"}, width={'size': 3, 'offset': 0, 'order': 2})

    ]),


  #figura 3 layout
    dbc.Row([
        dbc.Col(html.Div([html.H1("Top 15 Global Sales (Millions of Units)", style={'text-align': 'center',
                                                                                    'color':"#ffb703",
                                                                                    'font-family': title_font,
                                                                                    'font-size': 55}),
                          ])
                )]),



#### GRAPH
    dbc.Row([
        dbc.Col([dcc.Graph(id='my_line_chart', figure=fig_2)],style={'width': "100","margin": "20px",
            "background-color": color_box, 'box-shadow': shadow,
        'border-style': 'outset', 'border-color':'#80ffdb','border-width':'4px',
            "display":"incline-block"},
                width={'size':11, 'offset':0, 'order':1}),


    ], no_gutters=True, justify='start')



], fluid=True,
    style={'backgroundColor': back_color, })



# segunda pagina layout

page_2_layout =dbc.Container([
    dbc.Row([html.Div(id='page-2-content'),
             html.Br(),
             html.Button(dcc.Link('Go back to home', href='/'))

             ]),
    dbc.Row([dbc.Col(html.Div([html.H1('Credits', style={'text-align': 'center', 'color': "#FFFFFF",
                                                         'font-family': title_font,
                                                         'font-size': 70})])
                     )]),

    dbc.Row([
        dbc.Col(html.Div([html.H1('Here, you have the chance to take revenge on your favorite villains', style={'text-align': 'center','color':"#FFFFFF",
                                                                                                                "margin": "50px", 'font-family': title_font,
                                                                                                                'font-size': 55}),

                          ])
                )]),
    dbc.Row([
        dbc.Col([html.Div([
            DashCanvas(
                id='canvas-color',
                width=canvas_width,
                filename=filename,
                hide_buttons=['line', 'zoom', 'pan'],
            )
        ], style={'align-items': 'center'}),
            html.H2('Joana Rafael', style={"margin": "20px", 'color': "#FFFFFF", 'font-family': title_font,
                                           'font-size': 40}),
        html.H2('[20200588]', style={"margin": "20px", 'color': "#FFFFFF", 'font-family': def_font,'font-size': 17}),

        ], width={'size': 2, 'offset': 0, 'order': 1}, style={"margin": "20px"}),

        dbc.Col([html.Div([
            DashCanvas(
                id='canvas-color1',
                width=canvas_width,
                filename=filename1,
                hide_buttons=['line', 'zoom', 'pan'],
            )
        ], style={'align-items': 'center'}),
            html.H2('Daniel Correia', style={"margin": "20px", 'color': "#FFFFFF", 'font-family': title_font,
                                             'font-size': 40}),
        html.H2('[20200665]',style={"margin": "20px",'color':"#FFFFFF", 'font-family': def_font,'font-size': 17}),

        ], width={'size': 2, 'offset': 0, 'order': 1}, style={"margin": "20px"}),

        dbc.Col([html.Div([
            DashCanvas(
                id='canvas-color2',
                width=canvas_width,
                filename=filename3,
                hide_buttons=['line', 'zoom', 'pan'],

            )
        ], style={'align-items': 'center'}),
            html.H2('Henrique Costa', style={"margin": "20px", 'color': "#FFFFFF", 'font-family': title_font,
                                             'font-size': 40}),
            html.H2('[20200652]', style={"margin": "20px", 'color': "#FFFFFF", 'font-family': def_font,'font-size': 17}),

        ], width={'size': 2, 'offset': 0, 'order': 1}, style={"margin": "20px"}),

        dbc.Col([html.Div([
            DashCanvas(
                id='canvas-color3',
                width=canvas_width,
                filename=filename2,
                hide_buttons=['line', 'zoom', 'pan'],
            )
        ], style={'align-items': 'center'}),
            html.H2('Ricardo Santos', style={"margin": "20px", 'color': "#FFFFFF",
                                             'font-family': title_font,
                                             'font-size': 40}
                    ),
        html.H2('[20200620]', style={"margin": "20px", 'color': "#FFFFFF", 'font-family': def_font,'font-size': 17}),

        ], width={'size': 2, 'offset': 0, 'order': 1}, style={"margin": "20px"}),
        ]),
    dbc.Row([
        dbc.Col(html.Div([
        html.H6(children=['Brush width'],style={'color': "#FFFFFF"}),
        dcc.Slider(
            id='bg-width-slider',
            min=2,
            max=40,
            step=1,
            value=5
        ),
        daq.ColorPicker(
            id='color-picker',
            label='Brush color',
            value=dict(hex='#119DFF')
        ),
    ], className="three columns"))
        ],align="center"),
    html.Br(),  html.Br(),  html.Br(),

    dbc.Row([
        dbc.Col([html.Div(children=[
            html.Iframe(
                id='movie_player',
                src="https://giphy.com/embed/eJ4j2VnYOZU8qJU3Py",

                width="100%",
                height="600",

            ),
        ])
        ]),
        ]),


#dbc.Col(    html.Div([html.H1('Credits', style={'text-align': 'center','color':"#FFFFFF"})

],fluid=True,style={'backgroundColor': '#2C3539'})

####################################################
# callbacks para a tab

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return page_1_layout
    # You could also return a 404 "URL not found" page here

    # callbacks para a pintura


@app.callback(Output('canvas-color', 'lineColor'),
              Input('color-picker', 'value'))
def update_canvas_linewidth(value):
    if isinstance(value, dict):
        return value['hex']
    else:
        return value


@app.callback(Output('canvas-color', 'lineWidth'),
              Input('bg-width-slider', 'value'))
def update_canvas_linewidth(value):
    return value


## Canvas color 1
@app.callback(Output('canvas-color1', 'lineColor'),
              Input('color-picker', 'value'))
def update_canvas_linewidth(value):
    if isinstance(value, dict):
        return value['hex']
    else:
        return value


@app.callback(Output('canvas-color1', 'lineWidth'),
              Input('bg-width-slider', 'value'))
def update_canvas_linewidth(value):
    return value


## canvas color 2
@app.callback(Output('canvas-color2', 'lineColor'),
              Input('color-picker', 'value'))
def update_canvas_linewidth(value):
    if isinstance(value, dict):
        return value['hex']
    else:
        return value


@app.callback(Output('canvas-color2', 'lineWidth'),
              Input('bg-width-slider', 'value'))
def update_canvas_linewidth(value):
    return value


### canvas color 3
@app.callback(Output('canvas-color3', 'lineColor'),
              Input('color-picker', 'value'))
def update_canvas_linewidth(value):
    if isinstance(value, dict):
        return value['hex']
    else:
        return value


@app.callback(Output('canvas-color3', 'lineWidth'),
              Input('bg-width-slider', 'value'))
def update_canvas_linewidth(value):
    return value


# figura 2 callbacks
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output("table", "data"),
    Input("game_input", "value"),
    Input("my_slider", "value")
)
def update_table(game_input, my_slider):
    # not necessary anymore coz slide bar has always input!
    # if not game_input:
    # raise PreventUpdate

    if game_input:
        data = df_consoles[df_consoles['Name'].str.contains(game_input, na=False, case=False)]
        if my_slider:
            data = data[(data['Year'] >= my_slider[0]) & (data['Year'] <= my_slider[1])]

    if my_slider:
        data = df_consoles[(df_consoles['Year'] >= my_slider[0]) & (df_consoles['Year'] <= my_slider[1])]
        if my_slider:
            data = data[data['Name'].str.contains(game_input, na=False, case=False)]

    return data.to_dict("records")


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
