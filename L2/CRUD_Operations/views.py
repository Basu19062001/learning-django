from django.shortcuts import render

# Create your views here.
def core(request):
  names = [
            {'name':'Basudev', 'age':23},
            {'name':'Debu', 'age':56},
            {'name':'Kanan', 'age':49},
            {'name':'Kousik', 'age':15},
            {'name':'Pushpa', 'age':81},
            {'name':'Rumpa', 'age':25},
            {'name':'Kakali', 'age':29},
            {'name':'Sukla', 'age':27},
            {'name':'Snehasish', 'age':10},
            {'name':'Ziniya', 'age':3}
          ]
  text = "Minus saepe non consequuntur reiciendis sunt nesciunt earum dolor nobis optio harum, natus eum minus totam repudiandae sint facilis, iusto at ex nostrum excepturi. Deserunt ipsum possimus natus voluptate sint ipsa, excepturi quisquam alias quia minima, eius suscipit maiores quam rerum ducimus, eum nihil omnis vero, aspernatur dolorem nihil quae incidunt? Eum distinctio quam animi cupiditate natus repellendus autem dolorem. Maxime praesentium voluptates nisi adipisci quis alias mollitia aliquid optio vero officiis, optio quo cupiditate similique porro natus molestiae dolores cumque totam vero, dignissimos maiores iusto nemo quam architecto quia, ab tempora odio praesentium consectetur dolore officiis nobis mollitia et rerum, exercitationem sapiente repellat commodi assumenda iure eaque officia unde cumque hic. Distinctio iste voluptatem ipsum a quasi aperiam ducimus, aliquid soluta ut mollitia debitis vitae dolorem corrupti iure perferendis nulla ullam, ducimus iste libero neque facere amet ullam vitae magni eius esse, velit nulla quisquam similique, ex dolorum vitae earum reprehenderit est ratione molestias quas aspernatur consequuntur? Consequuntur fugit esse ex rem consectetur sit exercitationem fuga?"
  return render(request, 'app/core.html', context={'names' : names, 'page':'Core', 'text' : text})
  
def aboutt(request):
  context = {'page':'About'}
  return render(request, 'app/aboutt.html', context)

def contactt(request):
  context = {'page':'Contact'}
  return render(request, 'app/contactt.html', context)