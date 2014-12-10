from __future__ import unicode_literals

from rest_framework import serializers

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship
)


class PeopleSerializer(serializers.HyperlinkedModelSerializer):

    homeworld = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='planet-detail'
    )

    class Meta:
        model = People
        fields = (
            "id",
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld",
            "films",
            "species",
            "transport",
            "url",
        )


class PlanetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Planet
        fields = (
            "name",
            "rotation_period",
            "orbital_period",
            "diameter",
            "climate",
            "gravity",
            "terrain",
            "surface_water",
            "population",
            "residents"
        )


class FilmSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Film
        fields = (
            "title",
            "episode_id",
            "opening_crawl",
            "director",
            "producer",
            "characters",
            "planets",
            "starships",
            "vehicles",
            "species"
        )


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):

    homeworld = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='planet-detail'
    )

    class Meta:
        model = Species
        fields = (
            "name",
            "classification",
            "designation",
            "average_height",
            "skin_colors",
            "hair_colors",
            "eye_colors",
            "average_lifespan",
            "homeworld",
            "language",
            "people"
        )


class VehicleSerializer(serializers.HyperlinkedModelSerializer):

    pilots = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='people-detail'
    )

    class Meta:
        model = Vehicle
        fields = (
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "vehicle_class",
            "pilots"
        )


class StarshipSerializer(serializers.HyperlinkedModelSerializer):

    pilots = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='people-detail'
    )

    class Meta:
        model = Starship
        fields = (
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "hyperdrive_rating",
            "MGLT",
            "starship_class"
            "pilots"
        )
