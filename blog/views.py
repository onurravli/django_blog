from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def get_all_posts(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        dict(
            posts=[
                dict(
                    id=post.pk,
                    title=post.title,
                    content=post.content,
                    created_at=post.created_at,
                )
                for post in Post.objects.all()
            ]
        )
    )


def get_post(request: HttpRequest, post_id: int) -> JsonResponse:
    try:
        return JsonResponse(
            dict(
                id=Post.objects.get(pk=post_id).pk,
                title=Post.objects.get(pk=post_id).title,
                content=Post.objects.get(pk=post_id).content,
            )
        )
    except ObjectDoesNotExist as odne:
        return JsonResponse(
            dict(
                error="Post doesn't exist",
            ),
        )


def add_post(request: HttpRequest) -> JsonResponse:
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = timezone.now()
    try:
        Post.objects.create(
            Post(
                title,
                content,
                created_at,
            )
        )
        return JsonResponse(
            dict(
                message="Blog post created",
            )
        )
    except:
        return JsonResponse(
            dict(
                error="An error occurred",
            )
        )


@csrf_exempt
def post_handler(request: HttpRequest):
    m = request.method
    if m == "GET":
        return JsonResponse(
            dict(
                posts=[
                    dict(
                        id=post.pk,
                        title=post.title,
                        content=post.content,
                        created_at=post.created_at,
                    )
                    for post in Post.objects.all()
                ]
            )
        )
    elif m == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        created_at = timezone.now()
        try:
            if not title or not content or not created_at:
                return JsonResponse(
                    dict(
                        dict(
                            title=title,
                            content=content,
                            created_at=created_at,
                            body=request.POST,
                        ),
                        error="Required fields.",
                    ),
                )
            Post.objects.create(
                title=title,
                content=content,
                created_at=created_at,
            )
            return JsonResponse(
                dict(
                    message="Blog post created",
                )
            )
        except Exception as ex:
            return JsonResponse(
                dict(
                    error="An error occurred",
                    exception=ex.__str__(),
                )
            )
    else:
        return HttpResponse(
            JsonResponse(
                dict(
                    error="Method not allowed",
                )
            ),
            status=405,
        )
