# script para consultar api de mercado libre
import requests
import json
import datetime


class Consulta_API:
    def __init__(self):
        self.DATE=str(datetime.date.today()).replace('-','')

    
    def getKeyFromItem(self, item, key):
        """
        Recibo la key que necesito sacar del diccionario almacenado en item
        """
        return str(item[key]).replace('','').strip() if item.get(key) else "null"


    def get_most_relevant_items_for_category(self, category, output_file):
        """
        Recibimos los items mas relevantes por categoria.La variable category
        se le deberá asignar la categoría que queramos usar.
        La variable response termina transformandose en un json

        """
        url = (f'https://api.mercadolibre.com/sites/MLA/search?category={category}#json')
        response = requests.get(url).text
        response = json.loads(response)
        data = response["results"]

        with open(output_file, 'w', encoding='utf-8') as file:
            for item in data:
                _id = self.getKeyFromItem(item,'id')
                site_id = self.getKeyFromItem(item,'site_id')
                title = self.getKeyFromItem(item,'title')
                price = self.getKeyFromItem(item,'price')
                sold_quantity = self.getKeyFromItem(item,'sold_quantity')
                condition = self.getKeyFromItem(item,'condition')
                thumbnail = self.getKeyFromItem(item,'thumbnail')
                
                file.write(f'{_id}\t{site_id}\t{title}\t{price}\t{sold_quantity}\t{condition}\t{thumbnail}\t{self.DATE}\n')

# Ejemplo de uso de la clase
if __name__ == "__main__":
    consulta = Consulta_API()
    consulta.get_most_relevant_items_for_category('MLA438566', 'Python\Extraer_api_ML_SQL/file.tsv')