from .Cocktail_list import CocktailList
from .Cocktail_list_render import CocktailRenderList
from Cocktail.Cocktail_manual_output import OutputManual


cocktail_list = CocktailList(r'.\Cocktail\result.json')
data = cocktail_list.data
get_index_cocktail = cocktail_list.get_random_cocktail_list
