from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# view DB main page displays todo_list
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results} )
    
# displays newview add item
def create_an_item(request):
    
    if request.method=="POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()
    return render(request, "item_form.html", {'form': form})    
    
# displays in newview edit item w/ previous data
def edit_an_item(request, id):

    item = get_object_or_404(Item,pk=id)

    if request.method=="POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:        
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})  
# button toggle done    
def toggle_status(request, id):
    item = get_object_or_404(Item,pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
    
#

    
    
    
    
    
