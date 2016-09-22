def parse_citnet(infile_pub, infile_cit):
    """
    Parse the CitNetExplorer output files publications and citations

    Args:
        infile_pub: Publications filename
        infile_cit: Citations filename

    Returns:
        Two lists of lists. 
        
        The first one contains all publications in the format [id, author,
        year, doi, journal] and the second one all citations in the format
        [from_id, to_id].
    """
    id = 1
    publications = []
    citations = []
    with open(infile_pub, 'r') as f:
        next(f) # Skip first line, as that contains the header
        for line in f:
            conts = line.split('\t')
            publications.append([id, conts[0], conts[3], conts[4], conts[2]])
            id += 1
    with open(infile_cit, 'r') as f:
        next(f) # Skip first line, as that contains the header
        for line in f:
            conts = line.split()
            citations.append([conts[0], conts[1]])

    return publications, citations

def print_gml(publications, citations, outfile):
    """
    Print the network in GML format to outfile

    Args:
        publications: Publications array as given by parse_citnet
        citations: Citations list as given by parse_citnet
        outfile: Filename of the output file

    Returns:
        integer code: 0 for success, 1 for error
    """
    with open(outfile, 'w') as f:
        # Write constant output
        f.write('graph [\n')
        f.write('    directed 1\n')

        # Write nodes (publications)
        for pub in publications:
            f.write('    node [\n')
            f.write('        id {}\n'.format(pub[0]))
            f.write('        label "{}"\n'.format(pub[1]))
            f.write('        year {}\n'.format(pub[2]))
            f.write('        doi "{}"\n'.format(pub[3]))
            f.write('        journal "{}"\n'.format(pub[4]))
            f.write('    ]\n')
        
        # Write edges (citations)
        for cit in citations:
            f.write('    edge [\n')
            f.write('        source {}\n'.format(cit[0]))
            f.write('        target {}\n'.format(cit[1]))
            f.write('    ]\n')

        # Write finishing bracket
        f.write(']')
