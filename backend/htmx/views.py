# tasks_htmx/views.py
from django.shortcuts import render, get_object_or_404
from .models import Task, Message, Post
from .forms import MessageForm, PostForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.contrib.auth import get_user_model




def index(request):
    return render(request, 'htmx/index.html')




def user_info(request):
    if request.htmx:
        if request.user.is_authenticated:
            return HttpResponse(request.user.username)
        else:
            return HttpResponse('<span class="text-danger">Not logged in</span>')
    return HttpResponse(status=400)


def add_favorite(request):
    if request.method == "POST" and request.htmx:
        # Here you would add the favorite to the DB
        return HttpResponse(
            '<span class="text-success" _="on load add .pulse then wait 1s then remove .pulse">Added to favorites! <i class="fas fa-heart"></i></span>'
        )
    return HttpResponse(status=400)

def mark_read(request):
    if request.method == "POST" and request.htmx:
        # Logic to mark the notification as read
        return HttpResponse(
            '<span class="text-muted" _="on load add .fade-in then wait 1s then remove .fade-in">Marked as read <i class="fas fa-check-circle"></i></span>'
        )
    return HttpResponse(status=400)


# 🌟 Display all tasks
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, "htmx/task_list.html", {"tasks": tasks})

# ✅ Create a new task
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        task = Task.objects.create(title=title)
        html_content = render_to_string("htmx/partials/task_item.html", context={"task": task})
        return HttpResponse(html_content)

# ✏️ Toggle completion status

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return render(request, "htmx/partials/task_item.html", {"task": task})

# 🗑 Delete a task

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponse("")  # Return an empty response to remove the element





CITIZEN = {
    'id': 99,
    'first_name': 'John',
    'last_name': 'Doe',
    'ssn': '12345678',
    'date_of_birth': '2000/01/01',
}

def get_PR(request):
    citizen_id = request.GET.get('prid', '')

    if citizen_id == str(CITIZEN['id']):
        # ✅ Return an HTML response for HTMX
        return render(request, 'htmx/citizen_record.html', {'citizen': CITIZEN})
    
    # ✅ Ensure a response is always returned (handle invalid ID case)
    return HttpResponse("<p>Error: Citizen not found</p>", status=404)






def hello_world(request):
    return HttpResponse('Hello, World!')




def toggle_message(request):
    """Responds with either plain text or HTML based on alternating requests"""
    if request.headers.get("Accept") == "text/html":
        # Return HTML response
        html_content = render_to_string("htmx/partials/button_response.html")#not "render" to not send a full page
        return HttpResponse(html_content, content_type="text/html")
    else:
        # Return plain text response
        return HttpResponse("You received plain text!", content_type="text/plain")




def message_list(request):
    messages = Message.objects.all().order_by('-created_at')
    form = MessageForm
    return render(request, 'htmx/message_list.html', {"messages": messages, "form": form})

def message_add(request):
    if request.method == "POST":
        print("message_add Post ACESSED")
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            html_content = render_to_string(
                'htmx/partials/message_item.html',  # Render only the new message
                context={"m": message}
            )
            return HttpResponse(html_content)  # Return only the new message's HTML
        else:
            # If form is invalid, return validation errors as partial update
            print('incorrect method or form invalid')
                        # If form is invalid, return validation errors as partial update
            error_html = render_to_string(
                'htmx/partials/message_error.html', 
                context={"form": form}
            )  # Return only the new message's HTML
            return HttpResponse(error_html)






def post_list(request):
    form = PostForm()
    posts = Post.objects.all()
    return render(request, 'htmx/post_list.html', {"posts": posts, "form": form}) 




def post_search(request):
    if request.htmx:
        query = request.GET.get('query', '')
        query = escape(query)
        processed_results = []  # This will store our processed data
        
        if query:
            # Get the queryset (not modifying this)
            db_results = Post.objects.filter(title__icontains=query)[:10]
            
            # Process each result
            for post in db_results:
                highlighted = post.title.replace(
                    query, 
                    f'<span class="bg-warning">{query}</span>'
                )
                processed_results.append({
                    'title': mark_safe(highlighted),
                    'original': post
                })
        
        html_content = render_to_string(
            "htmx/partials/searched_post.html", 
            {"results": processed_results, "query": query}
        )
        return HttpResponse(html_content)



def post_like(request, post_id):
    if request.htmx:
        post = get_object_or_404(Post, id=post_id)
        post.likes += 1
        post.save()
        html_content = render_to_string("htmx/partials/like_button.html", {"post": post})
        return HttpResponse(html_content)



def post_create(request):
    if request.htmx:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            # Return a proper success response
            return HttpResponse(
                '<div class="alert alert-success">Successfully created!</div>'
            )
        else:
            # Return form with errors if validation fails
            return HttpResponse(
                render_to_string('htmx/partials/post_form_errors.html', {'form': form})
            )
    return HttpResponse("Invalid request", status=400)