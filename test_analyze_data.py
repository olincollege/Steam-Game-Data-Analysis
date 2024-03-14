import pytest
import pandas as pd

from analyze_data import (
    compare_game_genre_players,
    compare_price_ratings,
    compare_price_ratings_relevance,
    compare_price_num_players,
)

test_data = {
    "Game": [420, 380, 390],
    "Genre": [50, 40, 45],
    "Number of Players": [10, 20, 30],
    "Price": [399, 499, 599],
}

# load data into a DataFrame object:
df = pd.DataFrame(test_data)


# Define sets of test cases.
compare_game_genre_players_cases = []

compare_price_ratings_cases = []

compare_price_ratings_relevance_cases = []

compare_price_num_players_cases = []


# Define standard testing functions to check functions' outputs given certain
# inputs defined above.
@pytest.mark.parametrize("game,data", compare_game_genre_players)
def test_get_complement(game, data):
    """
    Test that a game maps to a correct genre, and to a correct number of
    players from a testing file.

    Given a string representing the title of a game, check that the
    compare_game_genre_players function correctly maps the
    string to a list with the first value being a string representing
    the games genre, and the second value being an int representing
    the number of players.

    Args:
        nucleotide: A single-character string equal to "A", "C", "T", or "G"
            representing a nucleotide.
        complement: A single-character string equal to "A", "C", "T", or "G"
            representing the expected complement of nucleotide.
    """
    result = get_complement(nucleotide)
    assert isinstance(result, str) and len(result) == 1
    assert result == complement


@pytest.mark.parametrize(
    "strand,reverse_complement", get_reverse_complement_cases
)
def test_get_reverse_complement(strand, reverse_complement):
    """
    Test that a string of nucleotides get mapped to its reverse complement.

    Check that given a string consisting of "A", "C", "T", and "G" that
    represents a strand of DNA, the get_reverse_complement function correctly
    returns the reverse complement of the string, defined as the complement of
    each nucleotide in the strand in reverse order.

    Args:
        strand: A string consisting only of the characters "A", "C", "T", and
            "G" representing a strand of DNA.
        reverse_complement: A string representing the expected reverse
            complement of strand.
    """
    result = get_reverse_complement(strand)
    assert isinstance(result, str)
    assert result == reverse_complement


@pytest.mark.parametrize("strand,rest", rest_of_orf_cases)
def test_rest_of_orf(strand, rest):
    """
    Test that a string representing a strand of DNA gets mapped to the rest of
    its open reading frame.

    Check that given a string representing a strand of DNA as defined above, the
    rest_of_orf function returns a string representing a strand of DNA for the
    rest of the given strand's open reading frame. This is the original strand
    until reading sets of three nucleotides results in a STOP codon, or the
    entire strand if no such codon appears when reading the strand.

    Args:
        strand: A string representing a strand of DNA.
        rest: A string representing the expected rest of the open reading frame
            of strand, or the entirety of strand if reading it does not result
            in a STOP codon at any point.
    """
    result = rest_of_orf(strand)
    assert isinstance(result, str)
    assert result == rest


@pytest.mark.parametrize("strand,orfs", find_all_orfs_one_frame_cases)
def test_find_all_orfs_oneframe(strand, orfs):
    """
    Test that a string representing a strand of DNA gets mapped to a list of all
    non-overlapping open reading frames (ORFs) aligned to its frame.

    Check that given a string representing a strand of DNA as defined above, the
    find_all_orfs_oneframe function returns a list of strings representing all
    non-overlapping ORFs in the strand that are aligned to the strand's frame
    (i.e., starting a multiple of 3 nucleotides from the start of the strand).
    Each ORF is a strand of DNA from a START codon to a STOP codon (or in the
    case of the last ORF in the strand, to the end of the strand if no STOP
    codon is encountered during reading).

    Args:
        strand: A string representing a strand of DNA.
        orfs: A list of strings representing the expected strands of DNA that
            are ORFs within strand's frame.
    """
    result = find_all_orfs_one_frame(strand)
    assert isinstance(result, list)
    assert Counter(result) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_cases)
def test_find_all_orfs(strand, orfs):
    """
    Test that a string representing a strand of DNA gets mapped to a list of all
    open reading frames within the strand, with no overlapping ORFs within any
    given frame of the strand.

    Check that given a string representing a strand of DNA as defined above, the
    find_all_orfs function returns a list of strings representing all ORFs in
    the strand as defined above. Overlapping ORFs are allowed as long as they do
    not occur in different frames (i.e., each ORF is only non-overlapping with
    the other ORFs in its own frame).

    Args:
        strand: A string representing a strand of DNA.
        orfs: A list of strings representing the expected strands of DNA that
            are ORFs within strand, with no overlapping ORFs within one frame of
            strand.
    """
    result = find_all_orfs(strand)
    assert isinstance(result, list)
    assert Counter(result) == Counter(orfs)


@pytest.mark.parametrize("strand,orfs", find_all_orfs_both_strands_cases)
def test_find_all_orfs_both_strands(strand, orfs):
    """
    Test that a string representing a strand of DNA gets mapped to a list of
    all open reading frames within the strand or its reverse complement, with no
    overlapping ORFs within a given frame.

    Check that given a string representing a strand of DNA as defined above, the
    find_all_orfs_both_strands function returns a list of strings representing
    all ORFs in the strand or its reverse complement as defined above.

    Args:
        strand: A string representing a strand of DNA.
        orfs: A list of strings representing the expected strands of DNA that
            are ORFs within strand or its reverse complement, with no
            overlapping ORFs within one frame of either.
    """
    result = find_all_orfs_both_strands(strand)
    assert isinstance(result, list)
    assert Counter(result) == Counter(orfs)


@pytest.mark.parametrize("strand,orf", find_longest_orf_cases)
def test_find_longest_orf(strand, orf):
    """
    Test that a string representing a strand of DNA gets mapped to a string
    representing the longest ORF within the strand or its reverse complement.

    Check that given a string representing a strand of DNA as defined above, the
    find_longest_orf function returns a string representing a strand of DNA
    equal to the longest ORF within the strand or its reverse complement.

    Args:
        strand: A string representing a strand of DNA.
        orf: A string representing a strand of DNA equal to the expected longest
            ORF in strand or its reverse complement.
    """
    result = find_longest_orf(strand)
    assert isinstance(result, str)
    assert result == orf


@pytest.mark.parametrize("strand,protein", encode_amino_acids_cases)
def test_encode_amino_acids(strand, protein):
    """
    Test that a string representing a strand of DNA gets mapped to a string
    representing the amino acids encoded by the strand.

    Check that given a string representing a strand of DNA as defined above, the
    encode_amino_acids function returns a string consisting of one-letter IUPAC
    amino acid codes corresponding to the sequence amino acids encoded by the
    strand.

    Args:
        strand: A string representing a strand of DNA.
        protein: A string representing the expected sequence one-letter IUPAC
            amino acid codes encoded by strand.
    """
    result = encode_amino_acids(strand)
    assert isinstance(result, str)
    assert result == protein
