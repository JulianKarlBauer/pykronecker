# Data
https://github.com/openjournals/joss-reviews/issues/4900#issuecomment-1299740253

# Commands
```
sudo docker run --rm \
    --volume $PWD:/data \
    --user $(id -u):$(id -g) \
    --env JOURNAL=joss \
    openjournals/paperdraft
```



## Review checklist for @JulianKarlBauer

### Conflict of interest

- [x] I confirm that I have read the [JOSS conflict of interest (COI) policy](https://github.com/openjournals/joss/blob/master/COI.md) and that: I have no COIs with reviewing this work or that any perceived COIs have been waived by JOSS for the purpose of this review.

### Code of Conduct

- [x] I confirm that I read and will adhere to the [JOSS code of conduct](https://joss.theoj.org/about#code_of_conduct).

### General checks

- [x] **Repository:** Is the source code for this software available at the [https://github.com/nickelnine37/pykronecker](https://github.com/nickelnine37/pykronecker)?
- [x] **License:** Does the repository contain a plain-text LICENSE file with the contents of an [OSI approved](https://opensource.org/licenses/alphabetical) software license?
- [x] **Contribution and authorship:** Has the submitting author (@nickelnine37) made major contributions to the software? Does the full list of paper authors seem appropriate and complete?
- [ ] **Substantial scholarly effort:** Does this submission meet the scope eligibility described in the [JOSS guidelines](https://joss.readthedocs.io/en/latest/submitting.html#substantial-scholarly-effort)
- [ ] **Data sharing:** If the paper contains original data, data are accessible to the reviewers. If the paper contains no original data, please check this item.
- [ ] **Reproducibility:** If the paper contains original results, results are entirely reproducible by reviewers. If the paper contains no original results, please check this item.
- [ ] **Human and animal research:** If the paper contains original data research on humans subjects or animals, does it comply with [JOSS's human participants research policy and/or animal research policy](https://joss.readthedocs.io/en/latest/policies.html?highlight=animal#joss-policies)? If the paper contains no such data, please check this item.


### Functionality

- [ ] **Installation:** Does installation proceed as outlined in the documentation?
- [ ] **Functionality:** Have the functional claims of the software been confirmed?
- [ ] **Performance:** If there are any performance claims of the software, have they been confirmed? (If there are no claims, please check off this item.)

### Documentation

- [ ] **A statement of need**: Do the authors clearly state what problems the software is designed to solve and who the target audience is?
- [ ] **Installation instructions:** Is there a clearly-stated list of dependencies? Ideally these should be handled with an automated package management solution.
- [ ] **Example usage:** Do the authors include examples of how to use the software (ideally to solve real-world analysis problems).
- [ ] **Functionality documentation:** Is the core functionality of the software documented to a satisfactory level (e.g., API method documentation)?
- [ ] **Automated tests:** Are there automated tests or manual steps described so that the functionality of the software can be verified?
- [ ] **Community guidelines:** Are there clear guidelines for third parties wishing to 1) Contribute to the software 2) Report issues or problems with the software 3) Seek support

### Software paper

- [x] **Summary:** Has a clear description of the high-level functionality and purpose of the software for a diverse, non-specialist audience been provided?
- [x] **A statement of need:** Does the paper have a section titled 'Statement of need' that clearly states what problems the software is designed to solve, who the target audience is, and its relation to other work?
- [ ] **State of the field:** Do the authors describe how this software compares to other commonly-used packages?
- [x] **Quality of writing:** Is the paper well written (i.e., it does not require editing for structure, language, or writing quality)?
- [ ] **References:** Is the list of references complete, and is everything cited appropriately that should be cited (e.g., papers, datasets, software)? Do references in the text use the proper [citation syntax](https://pandoc.org/MANUAL.html#extension-citations)?
