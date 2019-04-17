from prepare_data_1.addunitlength import prepare_data
from initial_point_2.main import init_point
from similar_unit_3.similar_unit import similar_unit
from special_lithology_4.special_lithology import special_lithology
from modifier_set1_5.biostratigraphy.biostratigraphy import biostratigraphy
from modifier_set1_5.vertical_proximity.vertical_proximity import vertical_proximity
from modifier_set1_5.lateral_proximity.lateral_proximity import lateral_proximity
from modifier_set1_5.stacking_pattern.stacking_pattern import stacking_pattern
from modifier_set2_6.associated_facies.associated_facies import associated_facies
from modifier_set2_6.lower_boundary.lower_boundary import lower_boundary
from modifier_set2_6.upper_boundary.upper_boundary import upper_boundary


def main():
    prepare_data()
    init_point()
    similar_unit()
    special_lithology()
    biostratigraphy()
    vertical_proximity()
    lateral_proximity()
    stacking_pattern()

    for i in range(0, 2):
        if i == 0:
            associated_facies("csv/stacking_pattern.csv", i + 1)
        else:
            associated_facies(f"csv/upper_boundary{i}.csv", i + 1)
        lower_boundary(f"csv/associated_facies{i + 1}.csv", i + 1)
        upper_boundary(f"csv/lower_boundary{i + 1}.csv", i + 1)


main()
