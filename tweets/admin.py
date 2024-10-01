from django.contrib import admin

from .models import Tweet, Like


# Register your models here.
class WordFilter(admin.SimpleListFilter):

    title = "Elon Musk Filter"

    parameter_name = "ElonMusk"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Contain Elon"),
            ("no", "exclude Elon"),
        ]

    def queryset(self, request, tweets):
        check_word1 = "elon"
        check_word2 = "musk"
        if self.value() == "yes":
            return tweets.filter(payload__contains=check_word1).filter(
                payload__contains=check_word2
            )
        elif self.value() == "no":
            return tweets.exclude(payload__contains=check_word1).exclude(
                payload__contains=check_word2
            )
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "like_count",
    )
    search_fields = [
        "user__username",
        "payload",
    ]
    list_filter = (
        "created_at",
        WordFilter,
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
    )

    search_fields = [
        "user__username",
    ]

    list_filter = ("created_at",)
