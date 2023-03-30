
import typing
from typing import List
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class NikeITPersonasCollectionAndSalesforceIn(BaseModel):
    data_sources: List[str]


class NikeITPersonasCollectionAndSalesforceOut(BaseModel):
    sent_to_salesforce: bool


class NikeITPersonasCollectionAndSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self,
        args: NikeITPersonasCollectionAndSalesforceIn,
        callbacks: typing.Any,
    ) -> NikeITPersonasCollectionAndSalesforceOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        sent_to_salesforce = results_dict[len(results_dict) - 1].sent_to_salesforce
        
        out = NikeITPersonasCollectionAndSalesforceOut(
            sent_to_salesforce=sent_to_salesforce
        )

        return out


load_dotenv()
nike_it_personas_app = FastAPI()


@nike_it_personas_app.post("/transform/")
async def transform(
    args: NikeITPersonasCollectionAndSalesforceIn,
) -> NikeITPersonasCollectionAndSalesforceOut:
    nike_it_personas_collection = NikeITPersonasCollectionAndSalesforce()
    return await nike_it_personas_collection.transform(args, callbacks=None)

