from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
import logging

from .models import RecipeBook, Recipe

logger = logging.getLogger("signals.py")


@receiver(post_save, sender=RecipeBook)
def set_recipe_book_permissions(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    logger.info("Creating permissions for RecipeBooks!")

    assign_perm(
        "view_recipebook",
        instance.owner,
        instance
    )

    assign_perm(
        "change_recipebook",
        instance.owner,
        instance
    )


@receiver(post_save, sender=Recipe)
def set_recipe_permissions(sender, instance, **kwargs):
    """Add object specific permission to the author"""
    logger.info("Creating permissions for Recipes!")

    assign_perm(
        "view_recipe",
        instance.recipe_book.owner,
        instance
    )

    assign_perm(
        "change_recipe",
        instance.recipe_book.owner,
        instance
    )
