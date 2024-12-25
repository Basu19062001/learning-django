from django.shortcuts import render

# Create your views here.
def first_app(request):
  return render(request, 'app/firstApp.html')

def person(request):
  people=[
    {'name':'Basudev Samanta', 'age': 23},
    {'name':'Kousik Santra', 'age': 15},
    {'name':'Kanan Samanta', 'age': 48},
    {'name':'Debu Samanta', 'age': 56},
    {'name':'Ziniya Manna', 'age': 3},
    {'name':'Puspa Samanta', 'age': 81},
    {'name':'Snehasish Santra', 'age': 10}
  ]
  text = """Iure incidunt hic soluta molestias ullam numquam ducimus, delectus possimus temporibus culpa architecto, odio unde beatae optio quos, cum consequatur minus officiis nulla possimus dolorem quas placeat deserunt laborum? Quasi magni debitis, cupiditate veritatis quae? Similique quo veniam excepturi corporis, nemo corporis non ex recusandae consectetur voluptatem quas neque eligendi culpa aperiam, quidem fuga accusamus facere praesentium totam est earum atque neque, natus iure sint, similique et neque amet beatae. Velit laboriosam deleniti perspiciatis, eveniet laborum facere officiis reiciendis ratione in officia nihil? Repellendus eius eum eveniet iste molestiae provident nam odio laboriosam doloribus debitis, eius minima libero quod dolorum explicabo debitis mollitia vitae quis numquam, magni saepe beatae quis nemo autem corporis nostrum delectus. Sapiente enim quae error cupiditate architecto soluta cumque quibusdam magni obcaecati, deleniti molestias architecto quos labore quidem dolore veniam a sint officiis. Quia eum sunt doloremque quis earum necessitatibus adipisci, tempora recusandae iusto, porro maxime nisi, suscipit rem dignissimos quis, debitis aliquid et repellendus? Saepe commodi obcaecati corporis iure rerum."""
  return render(request, 'app/people.html', context={'people' : people, 'text' : text})

def home(request):
  context = {'page':'Home'}
  return render(request, 'app/home.html',context)

def about(request):
  context = {'page':'About'}
  return render(request, 'app/about.html',context)

def auth(request):
  context = {'page':'Auth'}
  return render(request, 'app/auth.html',context)