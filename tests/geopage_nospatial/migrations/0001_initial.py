# Generated by Django 4.0.2 on 2022-02-20 16:35
import django.db.models.deletion
from django.db import migrations, models
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    import wagtail.blocks as wagtail_blocks
    import wagtail.fields as wagtail_fields
else:
    import wagtail.core.fields as wagtail_fields
    import wagtail.core.blocks as wagtail_blocks

import wagtailgeowidget.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="StandardPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StandardPageWithLeaflet",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        help_text="Search powered by Nominatim",
                        max_length=250,
                        null=True,
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StandardPageWithLeafletAndZoom",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        help_text="Search powered by Nominatim",
                        max_length=250,
                        null=True,
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StandardPageWithZoom",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("location", models.CharField(blank=True, max_length=250, null=True)),
                ("zoom", models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StreamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "body",
                    wagtail_fields.StreamField(
                        [
                            ("map", wagtailgeowidget.blocks.GoogleMapsBlock()),
                            ("map_leaflet", wagtailgeowidget.blocks.LeafletBlock()),
                            (
                                "map_struct",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GoogleMapsBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_with_deprecated_geopanel",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtail_blocks.CharBlock(required=True),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GeoBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_leaflet",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.LeafletBlock(
                                                address_field="address"
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_with_zoom",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "zoom",
                                            wagtailgeowidget.blocks.GeoZoomBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.GoogleMapsBlock(
                                                address_field="address",
                                                zoom_field="zoom",
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                            (
                                "map_struct_leaflet_with_zoom",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "address",
                                            wagtailgeowidget.blocks.GeoAddressBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "zoom",
                                            wagtailgeowidget.blocks.GeoZoomBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "map",
                                            wagtailgeowidget.blocks.LeafletBlock(
                                                address_field="address",
                                                zoom_field="zoom",
                                            ),
                                        ),
                                    ],
                                    icon="user",
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]
