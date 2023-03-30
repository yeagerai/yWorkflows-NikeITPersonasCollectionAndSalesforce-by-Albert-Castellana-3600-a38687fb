
import pytest
import typing

from core.workflows.nike_it_personas_collection import (
    NikeITPersonasCollectionAndSalesforce,
    NikeITPersonasCollectionAndSalesforceIn,
    NikeITPersonasCollectionAndSalesforceOut,
)


@pytest.mark.parametrize(
    "input_data_sources, expected_output",
    [
        (
            ["data_source_1", "data_source_2"],
            True,
        ),
        (
            ["data_source_3"],
            True,
        ),
        (
            [],
            False,
        ),
    ],
)
async def test_transform(
    input_data_sources: typing.List[str],
    expected_output: bool,
):
    # Create the component instance
    component = NikeITPersonasCollectionAndSalesforce()

    # Initialize the input and expected output data
    input_data = NikeITPersonasCollectionAndSalesforceIn(data_sources=input_data_sources)
    expected_data = NikeITPersonasCollectionAndSalesforceOut(
        sent_to_salesforce=expected_output
    )

    # Call the component's transform method with the mocked input and validate the result
    output_data = await component.transform(input_data, callbacks=None)
    assert output_data == expected_data

    # Error handling and edge case scenarios, if applicable
    if not input_data_sources:
        with pytest.raises(ValueError):
            await component.transform(args=None, callbacks=None)
